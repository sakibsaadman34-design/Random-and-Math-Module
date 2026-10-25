import random

while True:
    user_actions = input("Enter Rock, Paper Or Scissors: ")
    if (user_actions != "Rock" and user_actions != "Paper" and user_actions != "Scissors"):
        print("You can only choose either Rock, Paper or Scissors. If you did choose them, please capitalize the first letter.")
        continue
    possible_actions = ["Rock", "Paper", "Scissors"]
    computer_action = random.choice(possible_actions)
    print(f"You chose {user_actions}, Computer chose {computer_action}")

    if computer_action == "Rock":
        if user_actions == "Paper":
            print("Paper Covers Rock, You Win!")
        else:
            print(f"Rock Smashes {user_actions}, You Lose!")
    elif computer_action == "Paper":
        if user_actions == "Scissors":
            print("Scissors cut Paper, You Win!")
        else:
            print(f"Paper covers {user_actions}, You Lose!")
    elif computer_action == "Scissors":
        if user_actions == "Rock":
            print("Rock smashes Scissors, You Win!")
        else:
            print(f"Scissors cut {user_actions}, You Lose!")
    else:
        print("Something Went Wrong! Please try again.")
    play_again = input("Play again?(y/n): ")
    if play_again != "y":
        break