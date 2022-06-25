import os

def start_game(random_number, random_hint):
    print("Hint is.......", random_number - random_hint)

def check_results(user_input, random_number):
    if user_input < 10:
        print("Choose above 10!")

    if user_input > 100:
        print("Choose upto 100!")

    if user_input == random_number:
        print("You just won!")
        
    elif user_input != random_number:
        print("You lose!")
        print("Number was",random_number)
