# 3. Event Registration System: Design a program to manage registrations for an event. It should
# allow users to register by providing their name, email, and any additional required information.
# The program should track the number of registered participants, allow organizers to view
# registrations, and send confirmation emails to attendees.
fees = {}
info = {}
emails = {}

print('\t\t\t Event Registration System ')

def add():
    name = input('Enter your name: ')
    email = input('Enter your email: ')
    phone = int(input('Enter your phone number: '))
    print('Each person worth 100 rupees.')
    ppls = int(input('Enter the number of people, minimum 100: '))
    fees[name] = {'name': name, 'fees': ppls * 100}
    info[name] = {'username': name, 'user email': email, 'phone no': phone}
    print(f'All good, Mr. {name}. We will send you an email confirmation.')

def see():
    for name, inf in info.items():
        print(f"user: {inf['username']}, email: {inf['user email']}, phone no: {inf['phone no']} ")

def send():
    u = input('Enter the username you want to send an email to: ')
    d = input('Add description in the email: ')
    if u in fees:
        p = input(f'Should I add their payment {fees[u]["fees"]} fees? (y/n): ').lower()
        if p == 'y':
            pay = f' and Your payment is {fees[u]["fees"]}.'
            emails[u] = {'email': d + pay}
        elif p == 'n':
            emails[u] = {'email': d}
        else:
            pass
    else:
        print('User not found.')

def main():
    while True:
        print('Enter what you want to do:')
        print('Enter "r" to register, "s" to see registrations, "e" to send email, or any other key to exit.')
        choice = input('Enter choice: ').lower()
        if choice == 'r':
            add()
        elif choice == 's':
            see()
        elif choice == 'e':
            send()
        else:
            print('Goodbye.')
            break

main()
