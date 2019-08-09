'''
Project: factorial-finder.py
Purpose: Finds factorial of positive integer
Author: Brandon Lim
'''

def factorialRecursion(num):
    if num is 0:
        return 1
    else:
        return num * factorialRecursion(num - 1)


def factorialLoop(num):
    total = 1
    for i in range(1,num):
        total *= i
    return total 

def runner():
    print('This is a factorial calculator using recursion or loops. Enter the type of test (rec/loop): ')
    test = input()
    print('Enter a number to find the factorial: ')
    number = int(input())

    if test.lower() == 'rec':
        print(f'{factorialRecursion(number)} is the factorial of {number} using {test}.')
    elif test.lower() == 'loop': 
        print(f'{factorialLoop(number)} is the factorial of {number} using {test}.')
    else:
        print('Invalid type of factorial')


runner()