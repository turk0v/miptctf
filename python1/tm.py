password = 'e3f7d1980f611d2662d116f0891d7f3e'
print(password.lower())
if password.lower() != password:
    print('loser1')
elif len(password) != 32:    
    print('loser2')
else:
    if password != password[::-1]:
        print('loser3')
    try:
        if int(password[:16], 16) != 16426828616880430374:
            print('loser4')
    except:
        print('loser5')
    print('yooo')