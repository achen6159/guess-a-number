import random

#config
low = 1
high = 100
limit = 10

#helper functions
def get_guess():
    while True:
        guess = input("Take a guess: ")

        if guess.isnumeric():
            guess = int(guess)
            return guess
        else:
            print("You must enter a number")

def play_again():
    while True:
        decision = input("Would you like to play again? (y/n) ")

        if decision == "y" or decision == "yes":
            return True
        elif decision == "n" or decision == "no":
            return False

        print("I don't understand. Please answer 'y' or 'n')

again = True
              
while again:
    #start game
    rand = random.randint(low, high)
    print("I'm thinking of a number from " + str(low) + " to " + str(high));

    guess = -1
    tries = 0

    #play the game
    while guess != rand and tries < limit:
        guess = get_guess()
    
        if guess < rand:
            print("You guessed too low.")
        elif guess > rand:
            print("You guessed too high.")

        tries += 1
    #end the game
    if guess == rand:
        print("You win.")
    else:
        print("Aww...too bad. The number I was thinking of was " + str(rand) + ".")

    again = play_again()

print("Goodbye")



