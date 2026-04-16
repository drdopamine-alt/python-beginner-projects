import random
while True:
    user = input('Choose Yes/No: ') 
    if user == 'Yes':
        print(f'Your move is :{random.randint(1,6)}')
    elif user == 'No':
        print('Thank you for playing!')
        break
    else:
        print('Invalid input')