#!/usr/bin/env python3
from Crypto.PublicKey import RSA
import socket

multiple = 10


def to_hex(i):
    i_hex = hex(i)[2:]
    if len(i_hex) % 2 == 1:
        i_hex = '0' + i_hex
    return i_hex


def make_payload(n, e, cmd="getflag"):
    # RSA encode with chosen ciphertext attack
    Cx = int(cmd.encode().hex(), 16)
    Ca = pow(multiple, e, n)
    Cb = (Ca * Cx) % n

    # convert to byte array
    Cb_hex = to_hex(Cb)
    Cb = bytes.fromhex(Cb_hex)
    return Cb


def calculate_signature(n, e, sgn_multiplied):
    signature = sgn_multiplied // multiple
    if (signature * multiple != sgn_multiplied):
        # modulo division error, try adding n
        return calculate_signature(n, e, sgn_multiplied + n)
    verify = pow(signature, e, n)
    verify_text = bytes.fromhex(to_hex(verify))
    print("verify:", verify_text)
    return signature


if __name__ == '__main__':
    s = socket.socket()
    s.connect(('rsamachine.wpictf.xyz', 31337))

    # Bruteforce key length
    while True:
        data = s.recv(4096).decode().strip()
        if not data:
            break
        print("Received:", data)

        if '-----END PUBLIC KEY-----' in data:
            key = RSA.importKey(data)
            sign_text = make_payload(key.n, key.e)
            s.send(b'sign ' + sign_text + b'\n')

        if data.isdigit():
            sig = calculate_signature(key.n, key.e, int(data))
            s.send(b'getflag ' + str(sig).encode() + b'\n')
