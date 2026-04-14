user1 = input('Enter your move: ')
user2 = input('Enter your move: ')
if user1 == user2:
    pass
if user1 == 'Rock' and user2 == 'paper':
    print('user2 won')
if user1 == 'Rock' and user2 == 'scissor':
    print('user1 won')
if user1 == 'paper' and user2 == 'scissor':
    print('user2 won')
if user1 == 'paper' and user2 == '':
    print('user1 won')
