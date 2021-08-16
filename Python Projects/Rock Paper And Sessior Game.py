import random

choises = ["Rock", "Paper", "Sesior"]
computer = random.choice(choises)
player = False
player_score = 0
cpu_score = 0
while True:
    player = input("Rock, Paper or Sesior ?").capitalize()
    if player == computer:
        print("Tie !!")
    elif player == "Rock":
        if computer == "Paper":
            print("You Lose !!")
            cpu_score += 1
        else:
            print("You Win !!")
            player_score += 1

    elif player == "Sesior":
        if computer == "Rock":
            print("You Lose !!")
            cpu_score += 1
        else:
            print("You Win !!")
            player_score += 1
    elif player == "Paper":
        if computer == "Sesior":
            print("You Loose")
            cpu_score += 1
        else:
            print(" You Win !!")
            player_score += 1
    elif player == "End":
        print("** FINAL SCORE **")
        print(f"CPU : {cpu_score}")
        print(f"PLAYER : {player_score}")
        if cpu_score > player_score:
            print("COMPUTER WON")
        else:
            print("PLAYER WON")
        break



