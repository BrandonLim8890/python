'''
Author: Brandon Lim
Project: collatz.py
Description: starts with a number n > 1. Finds the number of steps it takes to reach one
'''

def collatz(num, count=0):
    if num <= 1:
        return count
    elif num % 2 == 0:
        return collatz(num / 2, count + 1)
    else:
        return collatz(num * 3 + 1, count + 1)


def runner():
    print('Enter a number above 1: ')
    answer = collatz(int(input()))
    print(f'The number of steps it took for the Collatz alg is {answer}')

runner()