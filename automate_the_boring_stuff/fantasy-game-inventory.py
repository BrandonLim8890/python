stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
inv = {'gold coin': 42, 'rope': 1}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def displayInventory(inventory):
    print('Inventory:')
    count_item = 0
    for k, v in inventory.items():
        print(f'{str(v)} {k}')
        count_item += v
    print(f'Total number of items: {count_item}')

def addToInventory(inventory, added_items):
    for item in added_items:
        inventory[item] = inventory.get(item, 0) + 1
    return inventory

inv = addToInventory(inv, dragon_loot)
displayInventory(inv)