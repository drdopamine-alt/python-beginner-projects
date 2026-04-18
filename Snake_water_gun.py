import random
#computer
rand_no = random.randint(1,3)
if rand_no == 1:
     computer = "snake"
elif rand_no == 2:
    computer = "water"
else:
    computer = "gun"

#USer-input
print("Choose: 1 for Snake, 2 for Water, 3 for Gun")
user_input = int(input("Enter your number: "))

if user_input == 1:
    user = "snake"
elif user_input == 2:
    user = "water"
elif user_input == 3:
    user = "gun"
else:
    user = "invalid"


print(f"\nYou chose: {user}")
print(f"Computer chose: {computer}")

if user == "invalid":
    print("That's not a valid number!")
elif user == computer:
    print("It's a Tie!")
elif (user == "snake" and computer == "water") or (user == "water" and computer == "gun") or (user == "gun" and computer == "snake"):
    print("You Win!")
else:
    print("You Lose!")