#Area finder of rectangle , ciclee, square and triangle.
options = ['Rectangle','Circle','Square','Triangle']
print(options)
choice = input('Enter your choice: ')
if choice == 'Rectangle':
    l = float(input('Enter length: '))
    b = float(input('Enter breadth: '))
    area = l*b
    print(f'Area of rectangle is {area}.')
elif choice == 'Square':
    side = float(input('Enter side of square: '))
    area = side*side
    print(f'Area of the square is {area}.')
elif choice == 'Circle':
    radius = float(input('Enter the radius of circle: '))
    area = 3.14*radius**2
    print(f'Area of cicle is {area}.')
else:
    base = float(input('Enter base: '))
    height = float(input('Enter height: '))
    area = 0.5*base*height
    print(f'Area of triangle is {area}.')