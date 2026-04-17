"""# Inputs
#total_rent
total_rent = int(input("Enter your total rent = "))
#Total food ordered
food_ordered = int(input("Enter your amount of food ordered = "))
#Electricity and per unit charfes
electricity = int(input("Enter your electricity bill amount = "))
charges_per_unit = int(input("Enter your charges per unit = "))
#Total bill
total_bill = electricity*charges_per_unit
#total person
people = int(input("Enter total members in your flat = "))
#output
output = (total_rent+food_ordered+total_bill)//people
print(output)"""


flatmates = int(input("Enter number of flatmates: "))
data = []
for i in range(flatmates):
    print(f"Enter details of flatmate{i+1}")
    name = input('Enter name: ')
    rent_paid = int(input("Enter rent paid: "))
    food_ordered = int(input("Enter your amount of food ordered = "))
    electricity = int(input("Enter your electricity bill amount = "))
    dict = {"Name": name, "Rent paid": rent_paid, "Food paid": food_ordered,"Electricity Paid": electricity}
    data.append(dict)
    print("Flatmate Data")
for i in data:
    print(i)
