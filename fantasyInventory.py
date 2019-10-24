##  Function that uses a dictionary to loop through a 
##  fantasy game inventory to count the total items.

stuff = {'arrow':12,'gold coin':42,
             'rope':1,'torch':6,'dagger':1}

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k,v in inventory.items():
        print(str(v) + ' ' + k)
        '''
        ##  Commented out input functionality, will add in a future version.
        newItem = input()
        stuff[newItem]
        print('Add quantity')
        itemQuantity = input()
        '''
        item_total += v
        print("Total number of items: " + str(item_total))
        
displayInventory(stuff)



