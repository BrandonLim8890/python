cat_list = []
while True:
    print('Enter the name of ' + str(len(cat_list) + 1) + ' (or press enter to stop)')
    name = input()
    if name is '':
        break
    else:
        cat_list += [name]
print('Cat names are:')
for cat in cat_list:
    print(cat)