# 6. Simple Travel Booking System: Design a program to help users book flights. It should allow
# users to search for flights based on origin, destination, and travel dates. The program should
# display available flights with details like airline, departure and arrival times, and price. Users
# should be able to choose a flight and book it (simulating the process).
flights = [
    {'airline': 'PIA (Pakistan International Airlines)', 'departure': '6:00 AM', 'arrival': '9:00 AM', 'price': 450, 'origin': 'asia'},
    {'airline': 'Delta Airlines', 'departure': '10:00 AM', 'arrival': '1:00 PM', 'price': 500, 'origin': 'asia'},
    {'airline': 'Air France', 'departure': '8:30 AM', 'arrival': '5:00 PM', 'price': 700, 'origin': 'europe'},
    {'airline': 'Japan Airlines', 'departure': '11:00 PM', 'arrival': '8:00 AM', 'price': 1000, 'origin': 'asia'},
    {'airline': 'British Airways', 'departure': '12:00 PM', 'arrival': '4:00 PM', 'price': 600, 'origin': 'europe'},
    {'airline': 'Emirates', 'departure': '3:00 AM', 'arrival': '2:00 PM', 'price': 800, 'origin': 'arabs'},
    {'airline': 'Qantas Airways', 'departure': '7:30 AM', 'arrival': '11:30 PM', 'price': 1200, 'origin': 'america'},
    {'airline': 'American Airlines', 'departure': '9:00 AM', 'arrival': '12:30 PM', 'price': 550, 'origin': 'america'},
    {'airline': 'Lufthansa', 'departure': '1:00 PM', 'arrival': '6:00 PM', 'price': 750, 'origin': 'idk'},
    {'airline': 'Singapore Airlines', 'departure': '4:30 AM', 'arrival': '3:30 PM', 'price': 1100, 'origin': 'asia'},
    {'airline': 'Cathay Pacific', 'departure': '2:00 PM', 'arrival': '10:00 PM', 'price': 900, 'origin': 'africa'}
]

def search():
    origin = input('Enter your origin: ').lower()
    print('The flights from your origin are: ')
    found = False
    for f in flights:
        if f['origin'] == origin:
            print(f"Airline: {f['airline']}, Departure: {f['departure']}, Arrival: {f['arrival']}, Price: {f['price']}, Origin: {f['origin']}")
            found = True
    if not found:
        print('Sorry, no flights found from your origin.')

def book():
    airline = input('Enter the airline you want to book: ').lower()
    destination = input('Enter your destination: ').lower()
    for f in flights:
        if f['airline'].lower() == airline:
            print(f"The flight with {f['airline']} is booked.")
            print(f"Departure time: {f['departure']}, Arrival time: {f['arrival']}. It goes to {destination}.")
            return
    print('Flight not found. Please try again.')

def view():
    for f in flights:
        print(f"Airline: {f['airline']}, Departure: {f['departure']}, Arrival: {f['arrival']}, Price: {f['price']}, Origin: {f['origin']}")

def main():
    while True:
        print('\t\t\tSimple travel booking system ✈')
        print('Available flights 🛫:')
        view()
        print('Enter "s" to search flights 🔎')
        print('Enter "b" to book flight 🛩')
        print('Enter anything else to quit.')
        reply = input('Enter your choice: ').lower()
        if reply == 's':
            search()
        elif reply == 'b':
            book()
        else:
            print('Goodbye.')
            break

if __name__ == "__main__":
    main()



