# 2. Library Management System: Create a program for a library to manage its books and users. It
# should allow adding new books with details like title, author, ISBN, and availability. The program
# should also register new users, track borrowed and returned books, and display available books
# based on various criteria like title, author, or genre.
books = [{'title': 'the brief history of time', 'author': 'stephen hawking', 'available': True},
         {'title': 'physics book', 'author': 'sir awaz', 'available': False}]
users = {}

def register():
    username = input('Enter your name: ').lower()
    if username in users:
        print(f'User {username} already exists!')
    else:
        password = input('Enter password: ')
        users[username] = password
        print('You have been successfully registered!')

def login():
    username = input('Enter your name: ').lower()
    if username not in users:
        print(f'User {username} not found!')
        return False
    password = input('Enter password: ')
    if users[username] == password:
        print(f'Welcome {username}!')
        return True
    else:
        print('Invalid password!')
        return False

def add_book():
    title = input('Enter the title of the book: ').lower()
    author = input('Enter the author name: ').lower()
    available = True  
    books.append({'title': title, 'author': author, 'available': available})
    print('Book added successfully!')

def display_books():
    for book in books:
        print(f"Title: {book['title']}, Author: {book['author']}, Available: {'Yes' if book['available'] else 'No'}")

def borrow_book():
    title = input('Enter the title of the book you want to borrow: ').lower()
    for book in books:
        if book['title'] == title:
            if book['available']:
                book['available'] = False
                print('Book borrowed successfully!')
            else:
                print('Book is not available for borrowing.')
            return
    print('Book not found!')

def return_book():
    title = input('Enter the title of the book you want to return: ').lower()
    for book in books:
        if book['title'] == title:
            if not book['available']:
                book['available'] = True
                print('Book returned successfully!')
            else:
                print('Book is already available.')
            return
    print('Book not found!')

def main():
    print('\t\tLibrary Management System')
    while True:
        print('\nType "R" to register, "L" to login, "A" to add books, "D" to display books, "B" to borrow book, "T" to return book, or "Q" to quit.')
        option = input('Enter your option: ').upper()
        if option == 'R':
            register()
        elif option == 'L':
            if login():
                break
        elif option == 'A':
            add_book()
        elif option == 'D':
            display_books()
        elif option == 'B':
            borrow_book()
        elif option == 'T':
            return_book()
        elif option == 'Q':
            print('Thank you for using the Library Management System!')
            break
        else:
            print('Invalid option!')

main()
