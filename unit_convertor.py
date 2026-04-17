#first we have to store the units in list or dictionary . then acces the dictory for every input and convert.
conversions = {("m","km"): lambda x: x/1000,("km","m"): lambda x: x*1000,("c", "f"): lambda x: (x*9/5)+32,("f", "c"): lambda x: (x-32)*5/9,("kg","g"): lambda x: x*1000,("g","kg"): lambda x: x/1000}


while True:
    value = float(input("Enter value: "))
    from_unit = input("From unit: ").lower()
    to_unit = input("To unit: ").lower()

    key = (from_unit, to_unit)

    if key in conversions:
        result = conversions[key](value)
        print(f"Result: {result}")
    else:
        print("Conversion not supported")

    again = input("Convert again? (yes/no): ").lower()
    if again != "yes":
        break

"""n = int(input('Enter a number: '))
unit = input('Enter the unit in Km or Kg: ')
if unit == 'Kg':
    print(f'The converted vaalue is {0.621371*n} miles.')
else:
    print(f'The converted value is {2.20462*n} pounds.')"""

"""while True:
    value = float(input("Enter value: "))
    
    print("Units: m (meters), km (kilometers)")
    from_unit = input("From unit: ").lower()
    to_unit = input("To unit: ").lower()

    if from_unit == "m" and to_unit == "km":
        result = value / 1000
    elif from_unit == "km" and to_unit == "m":
        result = value * 1000
    else:
        print("Invalid conversion")
        continue

    print(f"Result: {result}")

    again = input("Convert again? (yes/no): ").lower()
    if again != "yes":
        break"""
