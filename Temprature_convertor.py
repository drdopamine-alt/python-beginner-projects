dict = {('c','f'): lambda x : (x*9/5)+32, ('f','c'): lambda x : (x - 32)*5/9}
while True:
    temp = float(input('Enter your temprature: '))
    from_unit = input("From unit: ").lower()
    to_unit = input("To unit: ").lower()
    key = (from_unit, to_unit)

    if key in dict:
        result = dict[key](temp)
        print(f"Result: {result}")
        break
    else:
        print("Conversion not supported")

