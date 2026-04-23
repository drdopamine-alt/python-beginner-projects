#Store Product
product = {'Lipstick':200 , 'Blush': 350 , 'Perfume': 800 , 'Kajal':150 , 'Brasclet': 80}
#Store cart
cart = {} #This will store the quantity user purchase.
#Menu sysytem
print("Add item , \n Remove item , \n View cart , \n Checkout, \n Exit")
choose = input('Enter what you want to do!! ')
#Add items
if choose == 'Add item':
    items = input('Enter your item you purchased: ')
    quantity = float(input('Enter the quantity you buy: '))
    if items not in product:
        print("Item not available!")
    if items in cart:
        cart[items] += quantity
    else:
        cart[items] = quantity

    print("Item added!")
#Remove item
elif choose == 'Remove item':
    for i in cart:
        item = input("Enter item to remove: ").lower()

        if item in cart:
            del cart[item]
            print("Item removed!")
        else:
            print("Item not in cart!")
#View cart
elif choose == 'View cart':
    for item, qty in cart.items():
                price = product[item]
                print(f"{item} - {qty} x {price} = {qty * price}")
#Checkout
elif choose == "4":
    total = 0
    for item, qty in cart.items():
        total += product[item] * qty

    print("Total amount:", total)

# Exit
elif choose == "5":
    print("Thank you!")

else:
    print("Invalid choice!")


