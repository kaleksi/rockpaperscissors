from random import *

rock = "Rock"
paper = "Paper"
scissors = "Scissors"
guess = ""

rounds = 0
round_select = input("Welcome to Rock, Paper, Scissors! How many rounds would you like to play? \n")
round_select = int(round_select)

com_score = 0
plyr_score = 0



while rounds < round_select:

    roll = randint(1, 3)
    print("\n")
    if roll == 1:
        guess = input("Rock, Paper, Scissors, Shoot!\n")
        print("Computer throws " + rock)
        if guess == rock.lower():
            rounds += 1
            com_score += 1
            plyr_score += 1
            print("Tie!\n")
        if guess == paper.lower():
            rounds += 1
            plyr_score += 1
            print("You win!\n")
        if guess == scissors.lower():
            rounds += 1
            com_score += 1
            print("You lose!\n")

    if roll == 2:
        guess = input("Rock, Paper, Scissors, Shoot!\n")
        print("Computer throws " + paper)
        if guess == rock.lower():
            rounds += 1
            com_score += 1
            print("You lose!\n")
        if guess == paper.lower():
            rounds += 1
            plyr_score += 1
            com_score +=1
            print("Tie!\n")
        if guess == scissors.lower():
            rounds += 1
            plyr_score += 1
            print("You win!\n")

    if roll == 3:
        guess = input("Rock, Paper, Scissors, Shoot!\n")
        print("Computer throws " + scissors)
        if guess == rock.lower():
            rounds += 1
            plyr_score += 1
            print("You win!\n")
        if guess == paper.lower():
            rounds += 1
            com_score +=1
            print("You lose!\n")
        if guess == scissors.lower():
            rounds += 1
            plyr_score += 1
            com_score += 1
            print("Tie!\n")

if plyr_score > com_score:
    print("Game Over! You win " + str(plyr_score) + " to " + str(com_score))

if plyr_score < com_score:
    print("Game Over! You lose " + str(com_score) + " to " + str(plyr_score))

if plyr_score == com_score:
    print("Game Over! It's a tie! The score was " + str(plyr_score) + " to " + str(com_score))
