#This program lets the computer guess the number you're thinking of.
#
#Annie C.


import random

# config
low = 1
high = 1000


# helper functions
def show_start_screen():
    print("**************************")
    print("*  Guess a Number A.I.!  *")
    print("**************************")

def show_credits():
    pass
    
def get_guess(current_low, current_high):
    guess = ((current_high + current_low)//2)
    return guess

def pick_number():
    print("Think a number from " + str(low) + " to " + str(high) + ".")
    something_0 = input("Press enter when you're ready")

def check_guess(guess):
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

def show_result():
    print("I guessed the number right!")

def play_again():
    while True:
        decision = input("Would you like to play again? (y/n) ")

        if decision == 'y' or decision == 'yes':
            return True
        elif decision == 'n' or decision == 'no':
            return False
        else:
            print("I don't understand. Please enter 'y' or 'n'.")

def play():
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
show_start_screen()

playing = True

while playing:
    play()
    show_result()
    playing = play_again()

show_credits()



