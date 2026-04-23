import random
options = ['rock','paper','scissor']
def play_game():
    user = input('Enter your move: ')
    computer_choice = random.choice(options)
    print(f'computer chose:{computer_choice}')
    if user == computer_choice:
        print("It's a tie!")
    elif (user == 'rock' and computer_choice == 'scissor') or (user == 'scissor' and computer_choice == 'paper') or (user == 'paper' and computer_choice == 'rock'):
        print('user wins')
    else:
        print('computer wins')
    
play_game()