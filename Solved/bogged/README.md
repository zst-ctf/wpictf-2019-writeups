# bogged
Cryptography

## Challenge 
Two strange men called me last night. They call themselves the Bogdanoff twins. I don't know much about cryptocurrency- can you help them with their scheme?

nc bogged.wpictf.xyz 31337 (or 31338 or 31339)

made by rm -k
https://soundcloud.com/nanosmusics/one?in=nanosmusics/sets/p-o-r-n-o

> [leaked_source.py](leaked_source.py)

## Solution

References:

- https://github.com/zst123/crossctf_quals-2017-writeups/tree/master/Salted_Hash_Challenge
- https://github.com/zst123/gryphonctf-2017-writeups/tree/master/Solved/Saving_Gaia

When we connect to the service, we see this welcome message.

	Bonjour... 
	We have access to the Binance backdoor, and got you into a compromised teller station.
	We need you to steal tethered cryptocurrency from people's wallets.
	We were halted by an unfortunate countermeasure in the teller system, but we have an account ready to recieve the stolen crypto.

	Steal the currency from cryptowojak123. Transfer it to not_b0gdan0ff. 

	Transfer everything... then we will kill him, and find another.

	Do not fail us. 

We need to do a command of `withdraw cryptowojak123; deposit not_b0gdan0ff`.

From source code, we need to sign our commands. But we do not know the secret.

	def generate_command_token(command, secret):
	    hashed = hashlib.sha1(secret+command).hexdigest() 
	    return hashed

If we look at the transaction history, we see that we have the hashes of some combinations of `secret+command`. We can do a hash length extension attack

	///// TRANSACTION HISTORY //////////////////////////

	Command:
	>>>withdraw john.doe
	Auth token:
	>>>b4c967e157fad98060ebbf24135bfdb5a73f14dc
	Action successful!

	Command:
	>>>withdraw john.doe;deposit xXwaltonchaingangXx
	Auth token:
	>>>455705a6756fb014a4cba2aa0652779008e36878
	Action successful!

	Command:
	>>>withdraw cryptowojak123;deposit xXwaltonchaingangXx
	Auth token:
	>>>e429ffbfe7cabd62bda3589576d8717aaf3f663f
	Action successful!

	Command:
	>>>withdraw john.doe
	Auth token:
	>>>b4c967e157fad98060ebbf24135bfdb5a73f14dc
	Action successful!

We can do a length extension attack using the library hashpumpy in Python

Now we simply need to bruteforce the key length.

[solve.py](solve.py)

## Flag

	WPI{duMp_33t_aNd_g@rn33sh_H1$_wAg3$}
