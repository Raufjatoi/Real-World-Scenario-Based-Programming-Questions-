# 4. Simple Online Shop: Develop a program to simulate a basic online shop for selling products. It
# should display a list of available products with details like name, price, and quantity. The
# program should allow users to add items to their cart, view cart contents, and calculate the total
# cost.
items = [{'name': 'oranges', 'price': 120, 'quantity': 10},
         {'name': 'apples', 'price': 150, 'quantity': 12}]

def add():
    name = input('Enter the name: ').lower()
    price = int(input('Enter the price: '))
    quantity = int(input('Enter the quantity: '))
    for i in items:
        if name == i['name']:
            print('Name is already in the list. Do you want to update the price?')
            a = input('Enter reply y/n: ').lower()
            if a == 'y':
                price = int(input('Enter the new price: '))
                i['price'] = price
                print('Successfully updated.')
            return
    items.append({'name': name, 'price': price, 'quantity': quantity})
    print('Successfully added.')

def view():
    for i in items:
        print(f"Name: {i['name']}, Price: {i['price']}, Quantity: {i['quantity']}")

def total():
    print(f'Total items: {len(items)}')
    print(f'Total quantity: {sum(item["quantity"] for item in items)}')
    print(f'Total price of all items: {sum(item["price"] * item["quantity"] for item in items)}')

def main():
    print('\t\t\tSimple Online Shop 🛒')
    while True:
        print('Welcome to our shop. What do you want to do?')
        print('Type "a" to add an item.')
        print('Type "v" to view all items.')
        print('Type "t" to see totals.')
        print('Or anything else to exit. 😉')
        choice = input('Enter your choice: ').lower()
        if choice == 'a':
            add()
        elif choice == 'v':
            view()
        elif choice == 't':
            total()
        else:
            break

if __name__ == "__main__":
    main()
