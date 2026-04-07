#input for human 
#use random function 
import random
# computer 
num = random.randint(1,20)

#user gussing
m = int(input('Enter your number: '))
print(num)

if num == m:
    print('Congrats! you guess the correct number.')
elif num > m :
    print('you guess little higher.')
else:
    print('You guess a little lower.')
print('Game over!')