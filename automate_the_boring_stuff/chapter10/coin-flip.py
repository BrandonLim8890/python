import random
heads = 0
for i in range(1, 1001):
    if random.randint(0, 1) is 1:
        heads = heads +  1
    if i is 500:
        print('Halfway done!')
print(f'Heads came up {heads} times.')