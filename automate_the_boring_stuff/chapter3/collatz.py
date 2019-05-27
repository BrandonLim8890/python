def collatz(number):
    if number % 2 is 0: 
        print(str(number) +  " // 2")
        return number // 2
    else:
        print("3 * " + str(number) + " + 1")
        return 3 * number + 1

number = 0

while number is not 1:
    print('Enter a number: ')
    try:
        guess = int(input())
        number = collatz(guess)
    except ValueError:
        print('You did not use an integer')
    print(str(number))