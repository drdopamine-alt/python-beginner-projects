#House-Hold expense tracker 
#Menu options:- Add expenses, view expenses, Monthly total ,comparison of current and last month. 
#Add expense:- input(date, category, amount)
expense_list = []
def get_data():
    d = input('Enter date of spend: ')
    cat = input('Enter category: ')
    amount = float(input('Enter amount: '))
    return {'date':d,'category':cat, 'amt': amount}

def add_expenses():
    new_expenses = get_data()
    expense_list.append(new_expenses)
    print("Expenses added!")
def view_expenses():
    for i in expense_list:
        print(i)
def get_monthly_total():
    total = 0
    for item in expense_list:
        total += item['amt']
    print(f"Total expenses: {total}")

while True:
    print("Add expenses","View expenses","View Total spend","Exit")
    options = input("select an option: ")
    if options == 'Add expenses':
        add_expenses()
    elif options == 'View expenses':
        view_expenses()
    elif options == 'View Total spend':
        get_monthly_total()
    elif options == 'Exit':
        break
    else:
        print('Invalid option')

