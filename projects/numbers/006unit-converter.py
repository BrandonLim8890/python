'''
Name: unit-converter.py
Purpose: Enter the first unit, then converted unit and then value
Author: Brandon Lim
'''

def tempCalculator(input, output, value):
    if input == 'c' and output == 'f':
        return str(value * 9/5 + 32)
    elif input == 'f' and output == 'c':
        return str((value - 32) * 5/9)
    else:
        return 'Invalid types'

def currencyCalculator(input, output, value):
    if input == 'usd' and output == 'sgd':
        return str(value * 1.36)
    elif input == 'sgd' and output == 'usd':
        return str(value / 1.36)
    else:
        return 'Invalid types'

def volumeCalculator(input, output, value):
    if input == 'm3' and output == 'cm3':
        return str(value * 1000000)
    elif input == 'cm3' and output == 'm3':
        return str(value / 1000000)
    else:
        return 'Invalid types'

def massCalculator(input, output, value):
    if input == 'kg' and output == 'lb':
        return str(value * 2.205)
    elif input == 'lb' and output == 'kg':
        return str(value / 2.205)
    else:
        return 'Invalid types'


print('What do you want to convert? (Curr, mass, vol, temp): ')
conversion = input()

print('Enter the initial measurement: ')
initial = input()
print('Enter the converted measurement:')
output = input()
print('Enter the value to be converted: ')
val = input()

if conversion == 'curr':
    func = massCalculator
elif conversion == 'mass':
    func = massCalculator
elif conversion == 'vol':
    func = volumeCalculator
elif conversion == 'temp':
    func = tempCalculator

print(func(initial, output, val))
