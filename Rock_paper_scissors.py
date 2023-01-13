import random

def got_choices():
    user_choice = input("Rock Paper Scissors....Shoot: ")
    options = ["rock", "paper", "scissors"]
    computers_choice = random.choice(options)
    choices = {"user": user_choice, "computer": computers_choice}
    return choices

def check_win(user, computer):
    print(f"You have choose {user} and computer choose {computer}")
    if user == computer:
        return "Its a tie!"
    elif user == "rock":
       if computer == "scissors":
         return "You win! scissors have smashed by the rock"
       else:
        return "You lose! paper covers the rock"
    elif user == "paper":
       if computer == "rock":
         return "You win! paper wraps the rock"
       else:
        return "You lose! scissors cut the paper"
    elif user == "scissors":
       if computer == "paper":
         return "You win! scissors cut the paper"
       else:
        return "You lose! rock smashes the scissors"

choices = got_choices()

results = check_win(choices["user"], choices["computer"])

print(results)

