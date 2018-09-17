import re

def atoi(text):
    return int(text) if text.isdigit() else text
def natural_keys(text):
    return [ atoi(c) for c in re.split('(\s\d{2}\s)',text) ]

with open('alot.txt', 'r') as f:
	datastore = f.read()
searching_list = re.findall('[^.]* flag [^.]*\.',datastore)
searching_list.sort(key=natural_keys)
searching_list.pop(37)
searching_list.pop(36)
searching_list.pop(35)
searching_list.pop(34)
searching_list.pop(33)
searching_list.pop(32)
searching_list.pop(31)
searching_list.pop(30)
searching_list.pop(29)
searching_list.pop(28)
# final_list = []
# pattern = '/'(.*?)'/'
# for i in range(len(searching_list)):
# 	final_list.append(re.findall(pattern, searching_list[i]))
print((searching_list))


# flag{76bca453492f3b980572cedd66a46e59}