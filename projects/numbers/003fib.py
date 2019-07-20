'''
Name: fib.py
Purpose: Generate the Fibonacci sequence to the number provided
Author: Brandon Lim
'''

def fib(n):
    if n is 1:
        return 0
    elif n is 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

print('Ener a number to show the fibonacci sequence')
num = int(input())
print(fib(num))