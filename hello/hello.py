# price = 10 #int
# rating maximum.9 #float
# full_name = 'Brandon' #string
# is_published = True #boolean must bmaximumrue False
# print() #maximumnts something out


#------------------Inputs------------------
# name = input('What is your name? ')
# color = input('What is your favourite colour? ')
# print(name + ' likes ' + color)

# birth_year = input('Birth year: ') #takes in a string, not integer
# print(type(birth_year))
# age = 2019 - int(birth_year)
# print(type(age))
# print(age)


# weight = int(input('What is your weight in pounds? '))
# kilograms = weight * .453
# print(kilograms)

# course = '''
# Hi John,

# This is our first email.

# Thanks,
# Support Team

# '''

# hey = 'Python for Beginners'
# another = hey[:] # returns all the characters, so it copies it

# print(hey[0]) #first character of the stirng
# print(hey[-3]) #3rd last character of the string
# print(hey[0:3]) #goes from 0th index to 3rd index
# print(hey[1:]) # prints all characters from start index to end
# print(hey[5:]) # everything from 5th index on
# print(another)

# name = 'Jennifer'
# print(name[1:-1]) #Prints ennife from 1st index up to but not including -1st index

# ------------------Formatted Strings-------------------
# Dynamically adds values into strings
# first = 'John'
# last = 'Smith'
# message = first + ' [' + last + '] is a coder'
# msg = f'{first} [{last}] is a coder' # formated string with {placeholders} for strings
# print(msg)

# ------------------String Methods---------------------
# course = 'Python for Beginners'
# print(course.upper()) # upper doesnt change the original string
# print(course) # Still prints Python for Beginners
# print(course.find('Beginners')) # returns index of first appearance
# print(course.replace('Beginners', 'Absolute Beginners')) # Replaces things in strings
# print('python' in course) # returns boolean if string is in value
# print(course.title()) #title cases the string

# ------------------Operators-----------------------
# print(10 / 3) # gives a float 3.33333
# print(10 // 3) # returns integer 3
# print(10 ** 3) # returns 10 ^ 3

# ------------------Math Functions------------------
# import math

# x = 2.9
# print(round(x)) # rounds x
# print(abs(-2.9)) # absolute value

# ------------------If Else-------------------------
# is_hot = False
# is_cold = False

# if is_hot :
#     print("It's a hot day")
#     print('Drink plenty of water')
# elif is_cold :
#     print("It's a cold day")
#     print('Wear warm clothes')
# else :
#     print('It\'s a lovely day')
# print('Enjoy your day')

# good_credit = False
# house_price = 1000000

# if good_credit :
#     print(f'Required to put down ${0.10 * house_price}')
# else :
#     print(f'Required to put down ${0.20 * house_price}')

# ------------------Logical Operators-----------------------
# has_good_credit = True
# has_high_income = False
# has_criminal_record = False
# if has_high_income or has_good_credit: # Only 1 value must be true for OR
#     print('Eligible for loan')

# if has_high_income or has_good_credit: # Both values must be true
#     print('Eligible for loan')

# if has_good_credit and not has_criminal_record : # not operator is the same as !
#     print('Eligible for loan')

# ------------------Comparison operator------------------------
# temperature = 30

# if temperature > 30:
#     print("It's a hot day")
# else:
#     print("It's not a hot day")

# name = input('Enter your name: ')

# if len(name) < 3:
#     print('Name must be at least 3 characters long')
# elif len(name) > 50:
#     print('Name cannot exceed 50 characters')
# else:
#     print('Name looks good')

# weight = int(input('Weight: '))
# type_of_weight = input('L(bs) or K(g)').lower()
# if type_of_weight == 'k':
#     print(f'You are {weight * 2.20} pounds')
# elif type_of_weight == 'l':
#     print(f'You are {weight / 2.20} kilos')
# else:
#     print('Invalid type')

# ------------------While Loops-------------------------------
# secret_number = 9
# guess_count = 0
# guess_limit = 3
# while guess_count < guess_limit:
#     guess = int(input('Guess: '))
#     guess_count += 1
#     if guess == secret_number:
#         print('You won!!')
#         break
# else:
#     print('Sorry, you failed!') # Code will get executed after the while loop ends because it doesn't meet the condition anymore. Doesn't run after break

# user_input = input().lower()
# started = False
# while user_input != 'quit':
#     if user_input == 'start':
#             if started:
#                 print('Car is already started!')
#             else:
#                 print('Car started...Ready to go!')
#                 started = True
#     elif user_input == 'stop':
#         if not started:
#             print('Car is already stopped')
#         else:
#             started = False
#             print('Car stopped.')
#     elif user_input == 'quit':
#         break
#     elif user_input == 'help':
#         print("'start' - to start the car")
#         print("'stop' - to stop the car")
#         print("'quit' - to exit")
#     else:
#         print('Invalid input. Try again')
        
#     user_input = input().lower()

# ------------------------Forloops-------------------------------------
# for item in range(5,10,2): # (beginning, end not including, step)
#     print(item)
# price = [10, 20, 30]
# total = 0
# for item in price:
#     total += item
# print(f'Total: ${total}')

# ------------------------Nested Loops--------------------------------
# for x in range(3):
#     for y in range(2):
#         print(f'({x}, {y})')

# numbers = [5, 2, 5, 2, 2]
# for val in numbers:
#     output = ''
#     for x in  (val):
#         output += 'x'
#     print(output)

# -----------------------Lists-----------------------------------
# names = ['John', 'Bob', 'Mosh', 'Sarah', 'Mary']
# print(names[2:]) # square brackets with : dont modify the original array

# nums = [3, 4, 6, 6, 9, 11, 23, 1, 15]
# max = nums[0]

# for val in nums:
#     if max < val:
#         max = val
# print(f'{max} is the biggest number')

# -----------------------2DList---------------------------------
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# print(matrix[0][1])
# for row in matrix:
#     output = ''
#     for val in row:
#         output += str(val)
#     print(output)

# -----------------------List Functions--------------------------
# numbers = [5, 2, 1, 7, 4, 5, 3, 1]
# numbers2 = numbers.copy()
# numbers.append(10)
# Append - adds it at the end,
# Pop - removes the end
# insert - (index, object)
# print(numbers2)

# numbers = [5, 2, 1, 7, 4, 5, 3, 1, 5, 1, 7, 7]
# for num in numbers:
#     while numbers.count(num) > 1:
#         numbers.remove(num)
# print(numbers)

# unique = []
# for num in numbers:
#     if num not in unique:
#         unique.append(num)

# print(unique)

# --------------------Tuples----------------------------------
# numbers = (1, 2, 3, 4)
# numbers[0] = 10 # Can't mutate or change tuples
# print(numbers)

# ------------------------Unpacking-------------------------
# coordinates = (1, 2, 3)
# x = coordinates[0]
# y = coordinates[1]
# z = coordinates[2]

# x, y, z = coordinates # Shorthand of the code above
# # First item of the tuple and assigns it to the first variable, 2nd to 2nd

# print(y)

# ---------------------Dictionaries---------------------------
# customer = { # Keys should be unique
#     "name": "John Smith",
#     "age": 30,
#     "is_verified": True
# }
# customer['name'] = 'Jack Smith' # Ability to update
# customer['birthdate'] = 'Jan 1 1980'
# print(customer['name']) # Accesses values
# print(customer.get('birthdate', 'Jan 1 1980')) # If key does not exit, it returns None. Default value appears if there is no value

# phone = input('Phone: ')

# numbers = {
#     '1': 'One',
#     '2': 'Two',
#     '3': 'Three',
#     '4': 'Four'
# }

# ans = ''

# for char in phone:
#     ans += numbers.get(char, '!') + ' '
# print(ans)

# message = input('>')
# words = message.split(' ')
# emojis = {
#     ':)': '😊',
#     ':(': '😟'
# }
# output = ''
# for word in words:
#     output += emojis.get(word, word) + ' '
# print(output)

# -----------------------Functions--------------------------
# def greet_user(first_name, last_name): # Def only for functions, not variables
#     print(f'Hi {first_name} {last_name}!')
#     print('Welcome aboard')

# print('Start')
# greet_user(input('Enter your name >'), input('Last name >')) # order of inputs must match
# print('Finish')

# -------------------Keyword Arguements--------------------
# def greet_user(first_name, last_name):
#     print(f'Hi {first_name} {last_name}!')
#     print('Welcome aboard')

# print('Start')
# greet_user('John', 'Smith') # Positional arguements
# greet_user(last_name='Smith', first_name='John') # here, the order doesn't matter because first_name is assigned to John
# greet_user('John', last_name='Smith') # Can only use keyword arguments after positional. If not, errors are thrown

# --------------------Return Statement--------------------
# def square(number):
#     return number ** 2

# print(square(6))

# -------------------Reusable Functions------------------
# message = input('> ')

# def emoji_getter(input): 
#     emoji = {
#         ':)': '😊',
#         ':(': '😟'
#     }
#     words = input.split(' ')
#     output = ''
#     for word in words:
#         output += emoji.get(word, word) + ' '
#     return output

# print(emoji_getter(message))

# -----------------Exceptions----------------------
# try:
#     age = int(input('Age: '))
#     income = 20000
#     risk = income / age
#     print(age)
# except ZeroDivisionError: # if there is zero division error, don't crash the program
#     print('Age cannot be 0.')
# except ValueError: # if there is value error, the it prints this instead of crashing the program
#     print('Invalid value')

# -------------------Classes--------------------
# class Point: # Always use caps to start
#     def move(self): # Used to define functions
#         print("move")
#     def draw(self):
#         print('draw')


# point1 = Point()
# point1.x = 10 # Can assign new variables
# point1.y = 20
# print(point1.x)
# point1.draw()

# point2 = Point()
# point2.x = 1
# print(point2.x)

# ------------------Constructors---------------
# class Point:  # classes are always caps
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#     def move(self):
#         print('move')
#     def draw(self):
#         print('draw')

# point = Point(10, 20)
# point.x = 11
# print(point.x)

# class Person:
#     def __init__(self, name):
#         self.name = name
#     def talk(self):
#         print(f"Hi, My name is {self.name}")

# john = Person('John Smith')
# john.talk()

# bob = Person('Bob Smith')

# ----------------Inheritance--------------------
# class Mammal: 
#     def walk(self):
#         print('walk')

# class Dog(Mammal): # Classes in the parenthesis inherits the functions in the parent class
#     pass # This tells python to skip this line. Because it's inherited, we dont need to add anything but python thinks that the class is empty so it doesnt like it
#     def bark(self):
#         print('bark')

# class Cat(Mammal):
#     def be_annoying(self):
#         print('annoying') # Can also have individual functions

# cat = Cat()
# cat.be_annoying()

# ----------------Modules----------------------
# import converters # Brings in modules from another file.
# from converters import kg_to_lbs # Takes only the function

# kg_to_lbs(100)
# print(converters.kg_to_lbs(50)) # utils. accesses the files
# # Use modules to better organize code into seperate files


# import utils

# print(utils.find_max([1,3,2,4,5,33,21,21,312,312]))

# --------------------Packages-------------------
# Packages are a group of modules

# import ecommerce.shipping # package.shipping to access
# ecommerce.shipping.calc_shipping()

# from ecommerce.shipping import calc_shipping, calc_costs # makes calling functions much more easy
# calc_shipping

# from ecommerce import shipping # Imports the module, like doing import module
# shipping.calc_shipping()

# import package
# package.module.function
# from package import module
# module.function
# from package.module import function
# function

# ---------------------------------------------------
# import random
# random.random()# calls random function from 'random' modules

# class Dice:
#     def roll(self):
#         roll1 = random.randint(1,6)
#         roll2 = random.randint(1,6)
#         return roll1, roll2  # Returns a tuple

# dice = Dice()
# print(dice.roll())

# ----------------Files and Directories----------------
# from pathlib import Path

# # Absolute path
# # Windows: C:\Program Files\Microsoft
# # UNIX: /usr/local/bin

# path = Path()
# for file in path.glob('*'):
#     print(file)
