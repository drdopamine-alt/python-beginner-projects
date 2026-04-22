n = input('Enter word: ')
string = n.lower().strip()
palindrome = string[::-1]
if n == palindrome:
    print("It's a palindrome")
else:
    print("It's not a palindrome")