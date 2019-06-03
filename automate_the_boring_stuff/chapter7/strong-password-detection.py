import re

def strongPassDetect(password):
    upper_case = re.compile(r'[A-Z]')
    lower_case = re.compile(r'[a-z]')
    digit = re.compile(r'\d')
    if len(password) < 8:
        return 'Must be 8 characters or longer'
    if upper_case.search(password) is None:
        return 'Must have at least 1 upper case'
    if lower_case.search(password) is None:
        return 'Must have at least 1 lower case'
    if digit.search(password) is None:
        return 'Must have at least 1 digit'
    return True

while True:
    print('Enter a passsword: ')
    password = str(input())
    output = strongPassDetect(password)
    if output is True:
        print('Strong password')
        break
    else:
        print(f'Password not strong enough. {output}\n')
