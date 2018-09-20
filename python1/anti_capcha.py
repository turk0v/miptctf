import telnetlib
tn = telnetlib.Telnet('51.68.126.197', 5556)
for i in range(102):
	buf = tn.read_until(b' = ')
	equation = buf.split(b'\n')[-1]
	print(equation)
	equation = equation[:-3]
	result = str(int(eval(equation)))
	print("result is {}".format(result))
	tn.write(((result) + '\n').encode('ascii'))




