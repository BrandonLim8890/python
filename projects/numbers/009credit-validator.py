'''
Author: Brandon Lim
Project: credit-validator.py
Description: Validates credit card numbers by using the Luhn algorithm
'''

def luhnAlg(number):
    # Splits the number into an array of ints
    arr = [int(digit) for digit in str(number)]
    # Doubles every other digit
    for i in range(len(arr) - 2, -1, -2):
        arr[i] *= 2
        if arr[i] > 9:
            # Splits the double digit number into an array of ints
            temp_arr = [int(digit) for digit in str(arr[i])]
            # Sums the digits and assigns it back to the same spot
            arr[i] = sum(temp_arr)
    total = sum(arr)
    # Checks if the number provided is a valid number
    return total % 10 is 0
    

def runner():
    print('This is a credit card verifier. Please enter a credit card number to validate it: ')
    card_number = input()
    if luhnAlg(int(card_number)):
        print(f'The number {card_number} is a valid card number')
    else:
        print(f'The number {card_number} is not a valid card number')


runner()