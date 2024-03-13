# 5. Task Management App: Create a program to help users manage their tasks. It should allow
# adding new tasks with details like title, description, due date, and priority level. The program
# should display a list of tasks, allow marking tasks as completed, and filter tasks based on
# different criteria like due date or priority.

tasks = [{'title': 'do pushups', 'description': 'do 10 pushups daily', 'due date': '3/13/2024', 'mark': 'uncomplete', 'priority': 6}]

def new_task():
    title = input('Enter Title: ').lower()
    des = input('Enter description of title: ').lower()
    dd = input('Enter due date (ex: 3/13/2024): ').lower()
    pr = int(input('Enter priority out of 1/10: '))
    for t in tasks:
        if t['title'] == title:
            print('The title already exists. Do you want to change the due date? (y/n)')
            r = input('Enter reply: ').lower()
            if r == 'y':
                dd = input('Enter new due date (ex: 3/13/2024): ')
                t['due date'] = dd
                print('Updated successfully 🎉')
                return
            else:
                return
    else:
        tasks.append({'title': title, 'description': des, 'due date': dd, 'mark': 'uncomplete', 'priority': pr})
        print('Added successfully 🎉🍾')

def mark():
    title = input('Enter the title you want to mark: ').lower()
    for t in tasks:
        if t['title'] == title:
            t['mark'] = 'completed'
            print('All done 😁')
            return
    print('Didn\'t find the title 😟')

def view():
    for t in tasks:
        print(f"Title: {t['title']}, Description: {t['description']}, Due Date: {t['due date']}, Priority: {t['priority']}, Mark: {t['mark']}")

def impo():
    for t in tasks:
        if t['priority'] > 5:
            print(f"Title: {t['title']}, Description: {t['description']}, Due Date: {t['due date']}, Priority: {t['priority']}, Mark: {t['mark']}")

def les():
    for t in tasks:
        if t['priority'] < 5:
            print(f"Title: {t['title']}, Description: {t['description']}, Due Date: {t['due date']}, Priority: {t['priority']}, Mark: {t['mark']}")

def main():
    while True:
        print('\t\t\tTask management app')
        print('All tasks:')
        view()
        print('Enter "a" to add tasks ➕')
        print('Enter "i" to see important tasks ℹ')
        print('Enter "m" to mark tasks ✔')
        print('Enter "l" to see less important tasks 👇')
        print('Enter anything else to quit')
        reply = input('Enter your choice: ').lower()
        if reply == 'a':
            new_task()
        elif reply == 'i':
            impo()
        elif reply == 'm':
            mark()
        elif reply == 'l':
            les()
        else:
            print('Goodbye.... 👋')
            break

if __name__ == "__main__":
    main()

        
            
