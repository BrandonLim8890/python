#! python3
'''
Name: pi-nth-digit.py
Purpose: Get the value of Pi to n number of decimal places
Author: Brandon Lim
'''

import math

def nthDigit():
    print(f'Enter the number of decimals of pi you want to see')
    n = int(input())
    if n > 31:
        print('Too large of a number! Try again!')
        return nthDigit()
    elif n <= 0:
        print('Not valid')
        return nthDigit()
    else:
        return f'%.{n}f' % math.pi

print(nthDigit())
