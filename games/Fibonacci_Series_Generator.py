n = int(input('Enter your steps: '))
def steps(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    if n == 2:
        return 2
    else:
        return steps(n-1) + steps(n-2) + steps(n-3)
    
print('Number of ways you can put your steps: ', steps(n))
