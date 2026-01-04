import random

#rock paper scissors



user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors?   "))
#0, 1, 2

if user_choice == 0:
    print(f"You choose {user_choice} (Rock)")
elif user_choice == 1:
    print(f"You choose {user_choice} (Paper)")
elif user_choice == 2:
    print(f"You choose {user_choice} (Scissors)")



computer_choice = random.randint(0,2)
print(f"computer choice {computer_choice}" )

if computer_choice == 0:
    print("Rock")
elif computer_choice == 1:
    print("Paper")
elif computer_choice == 2:
    print("Scissors")


if user_choice >= 3 or user_choice <0:
    print("You type an invalid number. You lose!")
elif user_choice == 0 and computer_choice == 2:
    print("You win!😊")
elif computer_choice == 0 and user_choice == 2:
    print("You lose!🙁")
elif computer_choice > user_choice:
    print("You lose!🙁")
elif user_choice > computer_choice:
    print("You win!😊")
elif user_choice == computer_choice:
    print("It's a draw!😉")