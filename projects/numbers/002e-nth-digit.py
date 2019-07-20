'''
Name: e-nth-digit.py
Purpose: Get value of e to the n number of decimals
Author: Brandon Lim
'''

import math

def nthDigit():
    print('Enter the number of digits of e you want to view')
    n = int(input())
    if n > 31:
        print('Too large! Try again')
        return nthDigit()
    elif n <= 0:
        print('Invalid! Try again')
        return nthDigit()
    else:
        return f'%.{n}f' % math.e

print(nthDigit())