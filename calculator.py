#user input
#if, else 
#operators
#prblm:-
n = float(input('Enter a decimal value: '))
m = float(input('Enter second decimal value: '))
operator = input('Enter operator: ')
if operator == '+':
    print(n+m)
elif operator == '-':
    print(n-m)
elif operator == '*':
    print(n*m)
elif operator == '/':
    print(n/m)
else:
    print('Invalid operation')

