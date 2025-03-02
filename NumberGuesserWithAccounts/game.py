from random import randint
import sys
from Modules.println import *

sys.set_int_max_str_digits(0)

def GetDifficulty():
    difficulty = inputln("\nenter the difficulty you want to do\n1. easy (0 - 100)\n2. medium (0 - 1000)\n3. hard (0 - 10000)\n4. extreme (0 - 10000000)\n5. custom\n")
    while difficulty not in ["1","2","3","4","5"]:
        difficulty = inputln("\nenter the difficulty you want to do\n1. easy (0 - 100)\n2. medium (0 - 1000)\n3. hard (0 - 10000)\n4. extreme (0 - 10000000)\n5. custom\n")
    if difficulty == "1":
        return 0,100
    elif difficulty == "2":
        return 0,1000
    elif difficulty == "3":
        return 0,10000
    elif difficulty == "4":
        return 0,10000000
    else:
        def GetBounds():
            LowerBound = int(inputln("\nenter your lower bound: "))
            UpperBound = int(inputln("\nenter your upper bound: "))
            return LowerBound,UpperBound
        while True:
            try:
                LowerBound,UpperBound = GetBounds()
                while LowerBound > UpperBound:
                    println("\nyour lower bound cannot be bigger than your upper bound")
                    LowerBound,UpperBound = GetBounds()
                while LowerBound == UpperBound:
                    println("\nyour lower and upper bounds can not be the same")
                    LowerBound,UpperBound = GetBounds()

                return LowerBound,UpperBound
            except ValueError:
                print("\nyou must enter a number for your upper and lower bounds")

def win():
    pass

def game(LoggedIn,PlayedByBot = False):
    if not PlayedByBot:
        LowerBound,UpperBound = GetDifficulty()
        RandomNumber = randint(LowerBound,UpperBound)
    else:
        LowerBound,UpperBound = GetDifficulty()
        RandomNumber = randint(LowerBound,UpperBound)
        return RandomNumber,LowerBound,UpperBound
    attempts = 0

    def Logic(attempts):
        while True:
            try:
                guess = float(inputln(f"\nenter a guess between {LowerBound} and {UpperBound}: "))
                while guess > UpperBound or guess < LowerBound:
                    guess = float(inputln(f"\nenter a guess between {LowerBound} and {UpperBound}: "))
                    
                if guess != int(guess):
                    println("entered number must be a whole number")
                    continue

                attempts += 1
		        
                break
            except ValueError:
                println("\nguess must be an integer")

        if guess == RandomNumber:
            println(f"\nYou got the number correct, it took you {attempts} attempts.")
            attempts = 0
            win()
        elif guess > RandomNumber:
            println(f"\nYour guess is too big, guess a smaller number")
            Logic(attempts)
        else:
            println(f"\nYour guess is too small, guess a bigger number")
            Logic(attempts)
    Logic(attempts)

# the "Upper" and "Lower" variables is the range that the bot is guessing in within the binary search tree, thats why the GetGuess function returns the midpoint of the
# upper and lower variables, in the "game.py" file the "game()" function has a parameter called "PlayedByBot" that is set to False, we set it to True here because
# this is bot testing, after we are done testing we will delete this file and delete that parameter, if the paramter is set to True we end the game() function early
# by returning the random number

# the function for the logic in the bot tester is called "BotLogic()" so it doesnt conflict with the actual "Logic()" function

def GetGuess(Upper,Lower):
    return (Upper+Lower)//2

def BotLogic():
    attempts = 0
    RandomNumber,LowerBound,UpperBound = game(False,PlayedByBot = True)
    Upper,Lower = UpperBound,LowerBound

    while True:
        attempts += 1
        Guess = GetGuess(Upper,Lower)
        println(Guess)
        if Guess > RandomNumber:
            Upper = Guess
        elif Guess < RandomNumber:
            Lower = Guess
        else:
           println(f"Took {attempts} attempts for the bot")
           return
