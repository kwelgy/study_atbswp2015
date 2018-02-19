import pprint
import json

# def displayInventory(d):
#     print("Inventory:")
#     pprint.pprint(d)
#     print(json.dumps(d, indent=1).replace('"', ''))
#     print("Total number of items: " + str(len(d)))

def displayInventory(d):
    print("Inventory:")
    for k in d.items():
        print(str(k[1]) + ' ' + k[0])
    print("Total number of items: " + str(sum(d.values())))

def addToInventory(inventory, addedItems):
    for item in addedItems:
        inventory[item] = inventory.get(item, 0) + 1

stuff = {'rope': 1, 'torch': 6, 'gold coin' : 42, 'dagger': 1, 'arrow': 12}

displayInventory(stuff)

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'ruby']

addToInventory(stuff, dragonLoot)

displayInventory(stuff)