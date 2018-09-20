import telnetlib

tn = telnetlib.Telnet('51.68.126.197',30201)
buf = tn.read_all()