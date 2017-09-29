#This program lets you or the computer guess a number that the other one is thinking of
#
#Annie C.

import random
import math
def player_question():
    print("Would you like to guess a number or would you like the computer to guess a number?")
    response == str.lower(input("If you want to guess the number say me or if you want the computer to guess a number, say you."))
    if response == "me":
        ai = 0
    if response == "you":
        ai = 1
# config
if ai == 0:
    low = 1
    high = 100
    limit = math.ceil(math.log((high - low) + 1 , 2))

# helper functions
def show_start_screen():
    if ai == 0:
        print("**************************")
        print("**** Guess a Number ! ****")
        print("**************************")

def show_credits():
    if ai == 0:
        print("******************************************")
        print("**This awesome game was created by Annie**")
        print("******************************************")
    
def get_guess():
    if ai == 0:
        while True:
            guess = input("Guess a number: ")
            if guess.isnumeric():
                guess = int(guess)
                return guess
            else:
                print("You must enter a number.")

def pick_number():
    if ai == 0:
        print("I'm thinking of a number from " + str(low) + " to " + str(high) +".")
        print("You get " + str(limit) + " tries.")

        return random.randint(low, high)

def check_guess(guess, rand):
    if ai == 0:
        if guess < rand:
            print("You guessed too low.")
        elif guess > rand:
            print("You guessed too high.")

def show_result(guess, rand):
    if ai == 0:
        if guess == rand:
            print("You win!")
        else:
            print("You are such a loser! Looooooosssssseeeerrrr... The number was " + str(rand) + ".")

def play_again():
    if ai == 0:
        while True:
            decision = str.lower(input("Would you like to play again? (y/n) "))

            if decision == 'y' or decision == 'yes':
                return True
            elif decision == 'n' or decision == 'no':
                return False
            else:
                print("I don't understand. Please enter 'y' or 'n'.")

def play():
    if ai == 0:
        guess = -1
        tries = 0

        rand = pick_number()
    
        while guess != rand and tries < limit:
            guess = get_guess()
            check_guess(guess, rand)

            tries += 1

        show_result(guess, rand)


# config
if ai == 1:
    low = 1
    high = 100


# helper functions
def computer_show_start_screen():
    if ai == 1:
        print("**************************")
        print("*  Guess a Number A.I.!  *")
        print("**************************")

def computer_show_credits():
    if ai == 1:
        import time
        time.sleep(0.2)
        print("******************************************")
        time.sleep(0.2)
        print("**This awesome game was created by Annie**")
        time.sleep(0.2)
        print("******************************************")
    
    
def computer_get_guess(current_low, current_high):
    if ai == 1:
        guess = ((current_high + current_low)//2)
        return guess

def computer_pick_number():
    if ai ==  1:
        print("Think a number from " + str(low) + " to " + str(high) + ".")
        something_0 = input("Press enter when you're ready")

def computer_check_guess(guess):
    if ai == 1:
        print (guess)
        answer = str.lower(input("Tell me if my guess is too low, too high, or if it is correct"))
        if answer in ["low", "l"]:
            check = -1
            return check
        if answer in ["high", "h"]:
            check = 1
            return check
        elif answer in ["correct", "yes"]:
            check = 0
            return check
        else:
            print("I don't understand. Please say something smart.")
            print("This number below is still my guess though.")

def computer_show_result():
    if ai == 1:
        print("I guessed the number right!")

def computer_play_again():
    if ai == 1:
        while True:
            decision = input("Would you like to play again? (y/n) ")

            if decision == 'y' or decision == 'yes':
                return True
            elif decision == 'n' or decision == 'no':
                return False
            else:
                print("I don't understand. Please enter 'y' or 'n'.")

def computer_play():
    if ai == 1:
        current_low = low
        current_high = high
        check = -1

        pick_number()

        while check != 0:
            guess = get_guess(current_low, current_high)
            check = check_guess(guess)

            if check == -1:
                current_low = guess
            elif check == 1:
                current_high = guess
# Game starts running here
player_question()

show_start_screen()

playing = True

while playing:
    play()
    playing = play_again()

show_credits()
