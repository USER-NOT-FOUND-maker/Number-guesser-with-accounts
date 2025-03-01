from Modules.println import *
from AccountCreation import *
from game import *
from os import system

system("clear")

LoggedIn = False

println("If you ever want to exit for whatever reason, use the combination CTRL+C to exit the program overall or, if you are prompted to, enter the choice to 'exit'")

ExistingAccounts = GetAccounts()

CHOICES = ["1","2","3","4"]

def FailedLogin():
    println("Too many failed attempts. Login process is terminated.")

def LogIn():

    global LoggedIn
    global UserName

    try:

        println("if at any point you want to exit, click CTRL+C, this will shut down the application, just restart the application after")

        if ExistingAccounts == {}:
            return "No accounts exist"
        
        def GetUserName():
            UserName = inputln("enter the username of the account you want to log in to: ").strip()

            while UserName not in ExistingAccounts.keys():
                println("Username doesn't exist, try again")
                UserName = inputln("enter the username of the account you want to log in to: ").strip()
            
            return UserName
        
        UserName = GetUserName()
        NeededPassword = ExistingAccounts[UserName]
            
        def Authenticate():
            Attempts = 3
            while inputln("enter the password of this account: ") != NeededPassword:

                Attempts -= 1
                if Attempts == 0:
                    FailedLogin()
                    return False
                    
                println(f"Incorrect password, you are now on {Attempts} tries left, lose them and the login process WILL be terminated")

            return True

        if not Authenticate():
            return

        LoggedInAccount = {UserName:NeededPassword}

        LoggedIn = True
        return LoggedInAccount

    except KeyboardInterrupt:
        return "Terminated LOGIN process."

def GettingAction(LoggedIn):
    try:

        if not LoggedIn:
            choice = inputln("do you want to \n1. play as a guest\n2. log in to an account\n3. create an account\n4. clear screen\n5. exit\n")
            while choice not in CHOICES:
                println("Must enter a valid choice")
                choice = inputln("do you want to \n1. play as a guest\n2. log in to an account\n3. create an account\n4. clear screen\n5. exit\n")
        else:
            choice = inputln("do you want to \n1. play a game\n2. log out of this account\n3. clear screen\n4. exit\n")
            while choice not in CHOICES and choice != "4":
                println("Must enter a valid choice")
                choice = inputln("do you want to \n1. play a game\n2. log out of this account\n3. clear screen\n4. exit\n")

        return choice
    except KeyboardInterrupt:
        println("Exiting program!")
        exit()

def main(LoggedIn):
    try:
        global Account

        if LoggedIn:
            println(f"REMINDER! you are currently logged in as {UserName}")

        Action = GettingAction(LoggedIn)

        if not LoggedIn:

            if Action == "1":
                Choice = inputln("1. play yourself\n2. get bot to play\n")
                if Choice == "1":
                    game(False)
                else:
                    BotLogic()

            elif Action == "2":
                Account = LogIn()

            elif Action == "3":
                CreateAccount()

            elif Action == "4":
                system("clear")

            else:
                println("Exiting program!")
                exit()

        else:

            if Action == "1":
                game(True)

            elif Action == "2":
                LoggedIn = False
                Account = None

            elif Action == "3":
                system("clear")

            elif Action == "4":
                println("Exiting program!")
                exit()

    except KeyboardInterrupt:
        println("Exiting program!")
        exit()

while True:
    main(LoggedIn)
