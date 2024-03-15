# 9. Simple Social Media Feed: Design a program to represent a basic social media feed. It should
# allow users to post messages and view posts from other users (simulated data). Users should be
posts = [
    {'heading': 'Just completed my school life', 'date': '20/20/2020', 'likes': 10, 'comments': 12},
    {'heading': 'Excited for my upcoming trip to Paris!', 'date': '01/05/2021', 'likes': 25, 'comments': 8},
    {'heading': 'Started learning a new programming language today', 'date': '03/10/2021', 'likes': 15, 'comments': 5},
    {'heading': 'Celebrating my dog\'s birthday today', 'date': '07/15/2021', 'likes': 30, 'comments': 20},
    {'heading': 'Just got promoted at work!', 'date': '09/25/2021', 'likes': 50, 'comments': 18},
    {'heading': 'Reached 100k subscribers on YouTube!', 'date': '12/01/2021', 'likes': 100, 'comments': 50},
    {'heading': 'Started a new book club with friends', 'date': '02/14/2022', 'likes': 35, 'comments': 15},
    {'heading': 'Attended a fascinating tech conference today', 'date': '05/20/2022', 'likes': 40, 'comments': 10},
    {'heading': 'Visited the Grand Canyon for the first time', 'date': '08/10/2022', 'likes': 45, 'comments': 25},
    {'heading': 'Just finished renovating my kitchen!', 'date': '11/30/2022', 'likes': 55, 'comments': 30}
]

def select():
    c = input('Enter the name of post you wanna select: ').title()
    for p in posts:
        if p['heading'] == c:
            print(f"Post: {p['heading']}, posted in {p['date']}, likes = {p['likes']}, comments = {p['comments']}")
            action = input('Enter l to like the post, c to comment on the post, or any other key to go back: ').lower()
            if action == 'l':
                print('You liked the post.')
                p['likes'] += 1
            elif action == 'c':
                comment = input('Enter your comment: ')
                print('You added the comment.')
                p['comments'] += 1
            else:
                print('Returning to main menu...')
                break
            return
    print('Post not found.')

def view():
    print('\t\t\tSocial media 📱')
    for p in posts:
        print(f"Post: {p['heading']}, posted in {p['date']}, likes = {p['likes']}, comments = {p['comments']}")

def main():
    while True:
        view()
        choice = input('Enter "s" to select a post or anything else to quit: ').lower()
        if choice == 's':
            select()
        else:
            print('Bye bye! 🙋‍♂️')
            break

if __name__ == '__main__':
    main()


