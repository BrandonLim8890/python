'''
Name: prime.py
Purpose: Find all prime factors of a number inputted by the user
Author: Brandon Lim
'''

def findFactors(n):
    factors = [num for num in range(1, int(n / 2)) if n % num is 0 and prime(num)]
    return factors

def prime(num):
    if num is 2:
        return True
    elif num % 2 is 0:
        return False
    elif num is 1:
        return False
    
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i is 0:
            return False
    return True

print(f'Enter a number to find its prime factors')
number = int(input())

factors = findFactors(number)

if factors is None:
    print('No prime factors')
else:
    print(f'Prime factors of {str(number)} are: {factors}')