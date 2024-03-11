# 1. Restaurant Menu Management: Develop a program for a restaurant to manage its menu items.
# It should allow adding, removing, and updating menu items with details like name, price,
# description, and category (e.g., appetizer, main course, dessert). The program should also
# display the complete menu and filter items based on category.
items = {'biryani': 120, 'haleem': 130}

while True:
    print('\t\t\t Restaurant Menu Management ')
    a = input('What do you want to do?\n Enter:\n 1= To display menu\n 2= To edit menu\n 3= To display the actual dictionary\n Type "q" to quite \n Reply : ')
    if a == '1':
        for key, value in items.items():
            print(f'Item: {key}, price: {value}')
    elif a == '2':
        print(items)
        print('Enter A to add new items ')
        print('Enter R to remove somethin')
        print('Or just directly type item to update the price of it ')

        b = input('Enter wha ya wanna edit: ').lower()
        if b == 'r':
            c = input('Enter the item u wanna remove: ')
            if c in items:
                del items[c]
                print('sucessfuly removed')
                for key, value in items.items():
                   print(f'Item: {key}, price: {value}')
            elif c not in items:
                print('didnt find the item  ')
                pass
        elif b in items:
         d = int(input('Enter the updated price of it: '))
         items[b] = d
        elif b == 'a':
            add = input('Enter the item name ')
            price = int(input('Enter the price of tha item: '))
            if add not in items :
               items[add] = price
               print('Sucessfuly added ')
               for key, value in items.items():
                   print(f'Item: {key}, price: {value}')
            elif add in items :
                print('It already exists ')
                pass
    elif a == '3':
        print(items)
    elif a == 'q':
        break
        

