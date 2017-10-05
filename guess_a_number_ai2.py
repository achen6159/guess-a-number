#This program lets you or the computer guess a number that the other one is thinking of
#
#Annie C.

import random
import math
import time


game_play = True
while game_play:
    name = input("Please enter your name")
    print("Would you like to guess a number or would you like the computer to guess a number?")
    response = str.lower(input("If you want to guess the number say me or if you want the computer to guess a number, say you."))

    if response == "me":

        # config
        low = 1
        high = 100
        limit = math.ceil(math.log((high - low) + 1 , 2))

        # helper functions
        def show_start_screen(): 
            time.sleep(0.1)
            print("                 **********                   ")
            time.sleep(0.1)
            print("              ****************                ")
            time.sleep(0.1)
            print("           **********************             ")
            time.sleep(0.1)
            print("        ****************************          ")
            time.sleep(0.1)
            print("    ************************************      ")
            time.sleep(0.1)
            print("  ******************************************  ")
            time.sleep(0.1)
            print("         Guess a Number " + str(name) + "!    ")
            time.sleep(0.1)
            print("  *****************************************   ")
            time.sleep(0.1)
            print("    ************************************      ")
            time.sleep(0.1)
            print("        ****************************          ")
            time.sleep(0.1)
            print("           **********************             ")
            time.sleep(0.1)
            print("              *****************               ")
            time.sleep(0.1)
            print("                 ***********                  ")

        def show_credits():
            time.sleep(0.2)
            print("******************************************")
            time.sleep(0.2)
            print("**This awesome game was created by Annie**")
            time.sleep(0.2)
            print("**This was completed on the 4 of October**")
            time.sleep(0.2)
            print("******************************************")

        def get_guess():
            while True:
                guess = input("Guess a number: ")
                if guess.isnumeric():
                    guess = int(guess)
                    return guess
                else:
                    print("You must enter a number.")

        def pick_number():
            print("I'm thinking of a number from " + str(low) + " to " + str(high) +".")
            print("You get " + str(limit) + " tries.")

            return random.randint(low, high)

        def check_guess(guess, rand):
            if guess < rand:
                print(str(name) + ", You guessed too low.")
            elif guess > rand:
                print(str(name) + ", You guessed too high.")

        def show_result(guess, rand):
            if guess == rand:
                print(str(name) + ", You win!")
            else:
                print(str(name) + ", You are such a loser! Looooooosssssseeeerrrr... The number was " + str(rand) + ".")

        def play_again():
            while True:
                decision = str.lower(input("Would you like to play again? " + str(name) + "(y/n) "))

                if decision == 'y' or decision == 'yes':
                    return True
                elif decision == 'n' or decision == 'no':
                    return False
                else:
                    print("I don't understand. Please enter 'y' or 'n'.")

        def play():
            guess = -1
            tries = 0

            rand = pick_number()

            while guess != rand and tries < limit:
                guess = get_guess()
                check_guess(guess, rand)

                tries += 1

            show_result(guess, rand)
            
       # Game starts running here
        show_start_screen()

        playing = True

        while playing:

            play()
            playing = play_again()

        show_credits()
        game_play = False
        
    elif response == "you":
        
        # config
        low = 1
        high = 100
        


        # helper functions
        def show_start_screen():
            time.sleep(0.1)
            print("        *****************          ")
            time.sleep(0.1)
            print("    *************************      ")
            time.sleep(0.1)
            print("  *****************************    ")
            time.sleep(0.1)
            print(" ***** Guess a Number A. I.! ****  ")
            time.sleep(0.1)
            print("*********** " + str(name) + " ***********")
            time.sleep(0.1)
            print("  ******************************   ")
            time.sleep(0.1)
            print("    *************************      ")
            time.sleep(0.1)
            print("        *****************          ")

        def show_credits():
            import time
            time.sleep(0.2)
            print("******************************************")
            time.sleep(0.2)
            print("**This awesome game was created by Annie**")
            time.sleep(0.2)
            print("******************************************")


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
                print()
                print("This number below is still my guess though.")

        def show_result():
            print("I guessed the number right!")

        def play_again():
            while True:
                decision = input("Would you like to play again? " + str(name) +  "(y/n) ")

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
        game_play = False

    else:
        print("Please say me or you.")
