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
    """
    Return a truncated average of current low and high.
    """
    pass

def pick_number():
    print("Think a number from " + str(low) + " to " + str(high) + ".")
    something_0 = input("Press enter when you're ready")

    """
    Ask the player to think of a number between low and high.
    Then  wait until the player presses enter.
    """
    pass

def check_guess(guess):
    print (guess)
    answer = input("Tell me if my guess is too low, too high, or if it is correct")
    if "low" in answer:
        check = -1
    elif "high" in answer:
        check = 1
    else:
        check = 0
    return check
    """
    Computer will ask if guess was too high, low, or correct.

    Returns -1 if the guess was too low
             0 if the guess was correct
             1 if the guess was too high
    """

def show_result():
    """
    Says the result of the game. (The computer might always win.)
    """
    pass

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
    playing = play_again()

show_credits()



