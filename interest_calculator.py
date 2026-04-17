#get details
def get_details():
    amount = float(input('Enter your principal amount: '))
    time = float(input('Enter time in years: '))
    if time <= 1:
        rate = 0.05
    else:
        rate = 0.08
    return amount,time,rate
def simple_interest(p,t,r):
    return (p*t*r)/100

def compound_interest(p,t,r):
    n = 1 
    a = p*(1+r/n)**(n*t)
    return a - p

p,t,r = get_details()
si = simple_interest(p,t,r)
ci = compound_interest(p,t,r)
print(f'Simple Interest: {si:.2f}%')
print(f'Comound Interest: {ci:.2f}%')
