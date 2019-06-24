import random

guesses = ('tails', 'heads')

guess = ''
while guess not in (0, 1):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input
toss = random.randint(0, 1) # 0 is tails, 1 is heads
if guess is guesses[toss]:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = guesses.index(input())
    if guess is guesses[toss]:
        print('You got it')
    else:
        print('Nope. You are realy bad at this game')
        