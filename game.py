# rock paper scissors game

import random
import sys
import time


def main():
    play_again = "y"
    while play_again == "y":
        cog()
        play_again = input(
            "Would you like to play again? y/n : ").strip().lower()
    end_game()


def end_game():
    print("Thank you for playing!!")
    sys.exit()


def cog():
    user_input = get_user_input()
    machine_choice = get_random_input()
    match result(user_input, machine_choice):
        case 0:
            print("ERROR")
        case 1:
            print("USER WINS!!!")
        case 2:
            print("CPU WINS!!!")
        case 3:
            print("CLASHHH!!, ITS A DRAWWWWW")


def get_user_input():
    user_input = input("CHOOSE [rock/paper/scissors] : ").strip().title()
    print(f"User chose {user_input}!!!!")
    return user_input.lower()


def result(user_input, machine_choice):
    result = 0
    if user_input == machine_choice:
        result = 3
    elif (user_input == "rock" and machine_choice == "paper") or (user_input == "paper" and machine_choice == "scissors") or (user_input == "scissors" and machine_choice == "rock"):
        result = 2
    else:
        result = 1

    return result


def get_random_input():
    options = ["Rock", "Paper", "Scissors"]
    machine_choice = random.choice(options)
    print("Machine chose...")
    time.sleep(0.75)
    print("...")
    time.sleep(0.75)
    print("...")
    time.sleep(0.75)
    print(f"{machine_choice}!!!!")
    return machine_choice.lower()


if __name__ == "__main__":
    main()
