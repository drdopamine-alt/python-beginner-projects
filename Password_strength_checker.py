"""def strength_check():
    n = input('Enter your password: ')
    special = '!@#$%^&*'
    num = '123456789'
    if special in n:
        print('Your password strength is strong')
    elif num in n :
        print('Your password is not that strong!Change ypur password.')
    elif (num and special) in n:
        print('Your password is so strong!')
    else:
        print('Your passord is weak!')
strength_check() """


def strength_check():
    password = input("Enter your password: ")

    num = any(char.isdigit() for char in password)
    special = any(char in "!@#$%^&*" for char in password)
    upper_case = any(char.isupper() for char in password)
    lower_case = any(char.islower() for char in password)
    length = len(password)

    score = 0

    if length >= 8:
        score += 1
    if num:
        score += 1
    if special:
        score += 1
    if upper_case and lower_case:
        score += 1

    if score == 4:
        print("Very Strong Password")
    elif score == 3:
        print("Strong Password")
    elif score == 2:
        print("Moderate Password")
    else:
        print("Weak Password")


strength_check()