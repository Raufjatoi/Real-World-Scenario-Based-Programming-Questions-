# 10. Basic Expense Tracker: Develop a program to help users track their daily expenses. It should
# allow adding new expenses with details like date, category (e.g., food, transportation,
# entertainment), and amount. The program should categorize expenses, calculate total spending
# for different categories, and display statistics over a specified period.
exp = [{'name': 'today expense ', 'detail': 'broughth nothin cause of ramzan', 'expense' : 00 , 'date' : '12/20/2022', 'category' : 'home expense' } ]
def add ():
    a = input('Enter the name of exp : ').lower()
    for e in exp:
        if e['name'] == a:
            print('This expense is already in list try another name : ')
        elif e['name'] != a:
            pass
    d = input('Enter detail : ')
    e = int(input('Enter how much u spend on it :'))
    d = input('Enter date for rem ')
    c = input('Enter cat :  ex : home expense / outside expense :: ').lower()
    try:
         exp.append({'name': a , 'detail': d , 'expense': e , 'date': d , 'category' : c})
    except ValueError:
        print('an error occured sry ')
        pass
def view ():
    for e in exp:
        print(f" name : {e['name']} , detail : {e['detail']} , expense : {e['expense']} , date : {e['date']} cat :{e['category']} ")
def stat():
    a = 0
    b = 0
    for e in exp:
        if e['category'] == 'home expense':
            a += e['expense']
        else:
            pass
    print(f'Total expense based on home expense is {a} ')
    for e in exp:
        if e['category'] == 'outside expense':
            b += e['expense']
        else:
            pass
    print(f'Total expense based on outside expense is {b}')

def main ():
    while True:
     print('\t\t\t Basic Expense Tracker ♟')
     c = input('Enter v to view tasks or a to add or s to see the statics ORrr anythin else to quite : ').lower()
     if c == 'v':
         view()
     elif c == 'a':
         add()
     elif c == 's':
         stat()
     else:
         print('Have a nice dayy 🙋‍♂️')
         break
if __name__ == '__main__':
    main()
