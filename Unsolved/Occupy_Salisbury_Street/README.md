# Occupy Salisbury Street
Cryptography

## Challenge 

Did you know that while WPI is best known as a tech school, it is also the home of Worcester's banking hub? Opportunities can arise for the cunning CSC member to (il)legitimately make some money...

nc bank.wpictf.xyz 1337

pow code here: https://github.com/roboman2444/ctfpow/

made by rm -k
This is a President Challenge. See Prizes for more info.

## Solution

Relevant source code

	prec = 'wpictf2019pow'
	prec+= ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
	sham = ''.join(random.choices(string.ascii_lowercase, k=diff))

	m = hashlib.sha3_256()
	m.update(prec.encode("utf-8"))
	m.update(sham.encode("utf-8"))
	soldo = str(m.hexdigest())

	print('./powsolve.py ' + prec + ":" + str(diff) + ":" + soldo)


	solved = input('Enter solution:').strip()
	m = hashlib.sha3_256()
	m.update(solved.encode("utf-8"))
	if str(m.hexdigest()) != soldo:
		print("Given solution is not valid, must hash to " + soldo)
		exit(1)

Connect to server

	$ nc bank.wpictf.xyz 1337
	./powsolve.py wpictf2019pow4VCCSOX5ST:5:d7a6612d847769e797973803632d4529d8dd710db99686498ddb2efde212d362




## Flag

	??