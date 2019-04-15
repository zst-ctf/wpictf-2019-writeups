#!/usr/bin/env python3
import socket
from hashpumpy import hashpump


def getHash(extension, key_len):
    original_plaintext = 'withdraw john.doe'
    original_hash = 'b4c967e157fad98060ebbf24135bfdb5a73f14dc'

    new_hash = hashpump(original_hash, original_plaintext, extension, key_len)
    return new_hash


if __name__ == '__main__':
    s = socket.socket()
    s.connect(('bogged.wpictf.xyz', 31337))

    # Bruteforce key length
    key_len = 1
    while True:
        data = s.recv(4096).decode()
        if not data:
            break
        print("Received:", data)

        if 'Command:' in data:
            new_hash, new_pt = getHash(';withdraw cryptowojak123;deposit not_b0gdan0ff', key_len)
            new_hash = new_hash.encode()
            print('# key_len', key_len)
            print('# new_pt', new_pt)
            print('# new_hash', new_hash)
            s.send(new_pt + b'\n')
            s.send(new_hash + b'\n')
        if 'Error: Auth token does not match provided command' in data:
            key_len += 1
