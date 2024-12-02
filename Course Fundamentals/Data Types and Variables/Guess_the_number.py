import random

pc_num = random.randint(1, 100)
print("Do you want to play a game? Please answer with yes or no.")
user_answer = input()

def start_game():


    print("Guess the number :) hint for you: it is in the range from 1 to 100: ")
    while True:

        player_input = input()

        if not player_input.isdigit():
            print("Wrong input. Please type a number.")
            continue

        player_input = int(player_input)
        if player_input == pc_num:
            print("Well done! You guess it!")
            print("Do you want to play again? \n" "Please answer with yes or no.")
            user_answer_2 = input()
            if user_answer_2 == "yes":
                start_game()
            else:
                print("Have a great day!")
                break
        elif player_input > pc_num:
            print("Try again, this one is too high.")
        elif player_input < pc_num:
            print("Try again. This one is too low.")


if user_answer == "yes":

    start_game()
else:
    print("Have a great day!")

