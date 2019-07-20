'''
Name: next-prime.py
Purpose: Have the program look for the next prime number until the user stops
Author: Brandon Lim
'''

def isPrime(number):
    for i in range(2, int(number ** 0.5 + 1)):
        if number % i is 0:
            return False
    return True

def nextPrime(number=2):
    user = ''
    print('Hit enter to keep finding prime numbers')
    while user is '':
        while not isPrime(number):
            number += 1
        print(str(number))
        number += 1
        user = str(input())

print('Enter a starting number(Defualt value is 2):')
val = input()
if val is '':
    nextPrime()
else:
    nextPrime(int(val))