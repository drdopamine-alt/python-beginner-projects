num = int(input('Enter your number: '))
is_prime = True
for i in range(2,int(num**0.5)+1):
    if num%i == 0:
        is_prime = False
        break
if is_prime:
    print('It is a prime')
else:
    print('It is not a prime number.')