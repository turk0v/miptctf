import re
import requests

#levels from 10 to 50
html_cd = requests.get('http://51.68.126.197:51337/parrots?level=11&password=c45b63bdc3c5b9954d1796e1f8103ed0845c505b582d6bc235803f').text
for i in range(11,50):
	password = re.findall("(?s)(?<=<h3>)(.+?)(?=</h3>)", html_cd)[0].replace(" ", "")[4:].replace(":","=")
	k = i+1
	html_cd = requests.get('http://51.68.126.197:51337/parrots?level={}&{}'.format(k,password)).text
	print("level is {}".format(k))
	print("password is {}".format(password))

#levels 50 - 90
html_cd = requests.get('http://51.68.126.197:51337/parrots?level=50&password=8e8614058f111bbca1c2dc18cd46a58fe3b8fff8e4f157c0e0845b').text
for i in range(51,100):
	password = re.findall("(?s)(?<=<h2>)(.+?)(?=</h2>)", html_cd)
	for string in password:
		new_string = string.replace(" ","")
		if(re.findall("(?s)(?<=<h2>)(.+?)(?=</h2>)", requests.get('http://51.68.126.197:51337/parrots?level={}&password={}'.format((i),new_string)).text) == []):
			pass
		else:
			print(new_string)
			print("correct pass, moving to level {}".format(i))
			cor_pas = new_string
	html_cd = requests.get('http://51.68.126.197:51337/parrots?level={}&password={}'.format((i),cor_pas)).text

#level 91	 
html_cd = requests.get('http://51.68.126.197:51337/parrots?level=90&password=ab2d33a32d4a2c5161bdbf51348a7839ec3448a5a393ce3c93769e').text
password = re.findall("(?s)(?<=<h2>)(.+?)(?=</h2>)", html_cd)
for string in password:
		new_string = string.replace(" ","")
		print('http://51.68.126.197:51337/parrots?level=91&password={}'.format(new_string))

#levels 92-100
html_cd = requests.get('http://51.68.126.197:51337/parrots?level=91&password=c65d0872f955f2d237b226e1cf43ac519686b6bf3128bc9580c698').text
for i in range(92,101):
	password = re.findall(r'alt="(.*?)"',html_cd)
	result_pass = ''.join(str(elem) for elem in password)
	html_cd = requests.get('http://51.68.126.197:51337/parrots?level={}&password={}'.format(i,result_pass)).text
	print("new level is {} and password is {}".format(i,result_pass))




