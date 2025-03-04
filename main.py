import random
def game():
    
    random.seed(None)

    choices=["Stone","Paper","Scissors"]
    computer=random.choice(choices)
    player=input(f"Pick one: Stone, Paper, Scissors:  ").capitalize()
    print(f"computer picked {computer}")
    if player not in choices:
        print("Invalid Input! ")
    elif player == computer:
        print("It's a draw!")
        return
    elif (player=="Stone" and computer=="Scissors") or (player=="Paper" and computer=="Stone") or (player=="Scissors" and computer=="Paper"):
        print("You win!")
    else:
        print("You Lose!")

game()