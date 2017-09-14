import random

#config
low = 1
high = 100
limit = 10


#start game
rand = random.randint(low, high)
print("I'm thinking of a number from " + str(low) + " to " + str(high));

guess = -1
tries = 0

#play the game
while guess != rand and tries < limit:
    guess = input("Take a guess: ")
    guess = int(guess)
    
    if guess < rand:
        print("You guessed too low.")
    elif guess > rand:
        print("You guessed too high.")

    tries += 1  

#outcome of the game
if guess == rand:
    print("You win.")
else:
    print("Aww...too bad. The number I was thinking of was " + str(rand) + ".")




