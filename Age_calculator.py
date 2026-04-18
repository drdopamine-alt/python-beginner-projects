"""year = int(input('Enter your birth year: '))
current_year = int(input('Current year? '))
def get_age():
    print(current_year - year)
get_age()"""


year = int(input("Enter your birth year: "))
current_year = int(input("Current year? "))
get_age = lambda y, cy: cy - y
print("Your age is:", get_age(year, current_year))