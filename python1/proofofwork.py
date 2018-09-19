#Find such string X with len(X) = 8 that sha256('7ab1cba2' + X) has last 20 bits equal to 0.
from hashlib import sha256

def gen_all_hex():
    i = 0
    while i < 16**10:
        yield "{:08X}".format(i).lower()
        i += 1

        i += 1

zero_string = "00000000000000000000"
for s in gen_all_hex():
	string = '2fdc8549' + s
	hex_string = (sha256(str(string).encode('utf-8')).hexdigest())
	binary_string = bin(int(hex_string, 16))[2:].zfill(len(hex_string)*4)[-20:]
	if (binary_string == zero_string):
		print("youuhooo string is {}".format(string))
		break
	else:
		pass

