import random
import utils

while True:
    random_hint = random.randint(0, 5)
    random_number = random.randint(10, 100)
    print("═══════════════════════════════════\nGUESS THE NUMBER GAME\nType exit to quit the game")
    utils.start_game(random_number, random_hint)
    user_input = int(input("Enter a number between 10-100:"))
    utils.check_results(user_input, random_number)
