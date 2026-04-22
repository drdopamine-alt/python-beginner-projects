weight = float(input('Enter your weight in Kg: '))
height = float(input('Enter your height in meters: '))
bmi = weight//height**2
print(f'Your BMI is {bmi}.')
if bmi < 18.5:
    print('Your are underweight.')
elif 18.5 < bmi <25:
    print('You are normal weight.')
elif 25 <= bmi < 30:
    print('You are overweight.')
else:
    print('OMG! You are obese.')
