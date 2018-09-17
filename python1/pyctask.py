def check_password(password):
    if password.lower() != password:
        return False
    elif len(password) != 32:    
        return False
    else:
        if password != password[::-1]:
            return False
        try:
            if int(password[:16], 16) != 16426828616880430374:
                return False
        except:
            return False
        
        return True


password = input('Password: ')
if check_password(password):
    print('flag{%s}' % password)
else:
    print('Wrong!')