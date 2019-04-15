#!/usr/bin/env python3

def split_every_n(line, n):
    return [line[i:i+n] for i in range(0, len(line), n)]


def bin2ascii(inputs):
    return ''.join(map(lambda x: chr(int(x, 2)),
                   split_every_n(inputs, 8)))

def logic(Px, W, X, Y, Z):
	Wb = 0 if W else 1
	Xb = 0 if X else 1
	Yb = 0 if Y else 1
	Zb = 0 if Z else 1
	out = None

	# P0*WXY’ +
	# P0*W’YZ’+ P0*X’YZ’ +
	# P0*Y’Z +
	if Px == 0:
		out = (W*X*Yb) or (Wb*Y*Zb) or (Xb*Y*Zb) or (Yb*Z)

	# P1(W+X’+YZ)(X+Y’+Z’)(Y+Z)
	elif Px == 1:
		out = (W or Xb or Y*Z) and (X or Yb or Zb) and (Y or Z)

	# P2*W’XZ’ +
	# P2*W’Y +
	# coffee: X’, Y’, Z, P2
	# coffee: X, Y, Z’, P2
	elif Px == 2:
		out = (Wb * X * Zb) or (Wb * Y)

		# deduced
		out = (Wb * X * Zb) or (Wb * Y) or (Xb*Yb*Z) or (X*Y*Zb)
	

	# P3 * X +
	# coffee: P3, Y, Z'
	# coffee: P3, Y', Z
	elif Px == 3:
		out = X

		# deduced
		out = X or ((Y*Zb) ^ (Yb*Z))


		# due to coffee spill, we don't know the 0s
		#if not out:
		#	out = None

	# P4(W’+X’+Z)(W+X’+Y’)(X+Y’+Z’)(X+Y+Z)
	elif Px == 4:
		out = (Wb or Xb or Z) and (W or Xb or Yb) and (X or Yb or Zb) and (X or Y or Z)

	# P5(X’+Y’+Z)(X’+Y+Z’)(X+Y+Z)
	# Dont care if P5*W
	elif Px == 5:
		if not W:
			out = (Xb or Yb or Z) and (Xb or Y or Zb) and (X or Y or Z)

	if out is None:
		return None

	if out:
		return 1
	else:
		return 0

flag = ''
for Px in range(0b000, 0b111+1):
	# don't care
	if Px == 6:
		continue
	if Px == 7:
		continue

	'''
	A = Px & (1<<2)
	B = Px & (1<<1)
	C = Px & (1<<0)
	'''
	#flag = ''
	for WXYZ in range(0x0, 0xF+1):
		W = 1 if (WXYZ & (1<<3)) else 0
		X = 1 if (WXYZ & (1<<2)) else 0
		Y = 1 if (WXYZ & (1<<1)) else 0
		Z = 1 if (WXYZ & (1<<0)) else 0

		Output = logic(Px, W, X, Y, Z)

		if Output is not None:
			flag += str(Output)

		print(f'Px={bin(Px)[2:].zfill(3)}, Sel={W}{X}{Y}{Z} => {Output} ')


	flag_ascii = bin2ascii(flag)
	print(f'Px={bin(Px)[2:].zfill(3)}', flag)
	print(f'Px={bin(Px)[2:].zfill(3)}', flag_ascii)
	print('====================================')



flag_ascii = bin2ascii(flag)
print(f'Flag', flag_ascii)


