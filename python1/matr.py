import json
import binascii
import base64


with open('matryoshka.json','br') as f:
	datastore = json.load(f)
i = 0
while (i < 50):
	if (datastore['type'] == 'base64'):
		datastore = base64.b64decode(datastore['data'])
		datastore = json.loads(datastore)
		i=+1
	elif (datastore['type'] == 'base85'):
		datastore = base64.b85decode(datastore['data'])
		datastore = json.loads(datastore)
		i=+1
	elif (datastore['type'] == 'hex'):
		datastore = binascii.unhexlify(datastore['data'])
		datastore = json.loads(datastore)
		i=+1
	else:
		print(datastore)

# q00,q10,q01,q11,q20,q21
# 1,2,3,4,5,6




# with open('mat.txt','w') as b:
#  	b.write(str(message_decoded))
