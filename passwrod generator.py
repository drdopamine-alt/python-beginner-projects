import string
import random
pass_length = int(input('Enter the lenght of your password: '))
chara = string.ascii_letters + string.digits
password = ''
for i in range(pass_length):
    password += random.choice(chara)
print('The password is:  ',password)
