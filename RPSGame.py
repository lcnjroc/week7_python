from random import randint

comphealth = 3
playerhealth = 3
X = 0


# available weapons => store this in an array
choices = ["Rock", "Paper", "Scissors"]
player = False


# make the computer pick one item at random!
computer = choices[randint(0, 2)]


# show the computer's choices in the terminal window
print("Computer chooses: ", computer)


while player is False:
    print("Choose your tool!\n")
    player = input("Rock, Paper, Scissors?\n")
    print("Player chooses:", player)
    print("Player Health " + str(playerhealth))
    print("Computers Health " + str(comphealth))

    if (player == computer):
        print("Computer chooses: ", computer)
        print("Draw! Live to play another day")

    elif player == "Rock":
        if computer == "Paper":
            print("Computer chooses: ", computer)
            print("You lost the round,", computer, "covers", player)
            playerhealth = playerhealth - 1
        else:
            print("Computer chooses: ", computer)
            print("You won the round,", player, "destroys", computer)
            comphealth = comphealth - 1

    elif player == "Paper":
        if computer == "Scissors":
            print("Computer chooses: ", computer)
            print("You lost the round,", computer, "chops", player)
            playerhealth = playerhealth - 1

        else:
            print("Computer chooses: ", computer)
            print("You won the round,", player, "covers", computer)
            comphealth = comphealth - 1
         

    elif player == "Scissors":
        if computer == "Rock":
            print("Computer chooses: ", computer)
            print("You lost the round,", computer, "destroys", player)
            playerhealth = playerhealth - 1
           
        else:
            print("Computer chooses: ", computer)
            print("You won the round,", player, "chops", computer)
            comphealth = comphealth - 1      

    elif player == "quit":
        exit()


    else:
        print("Not a valid choice. Check again, and check your spelling!\n")


    player = False
    computer = choices[randint(0, 2)]


    if comphealth is X:
        print("You Won!")
        player = input("Would you like to try again? y / n\n")
        comphealth = comphealth + 3
        playerhealth = comphealth
        if player == "y":
            player = False
        if player == "n":
            break


    if playerhealth is X:
        print("You Lost!")
        player = input("Would you like to try again? y / n\n")
        playerhealth = playerhealth + 3
        comphealth = playerhealth
        if player == "y":
            player = False
        if player == "n":
            break
