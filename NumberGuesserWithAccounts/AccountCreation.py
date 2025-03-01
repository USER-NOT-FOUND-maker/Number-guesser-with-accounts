from string import punctuation,digits,ascii_lowercase,ascii_uppercase
from Modules.XorEncrypt import encrypt
from Modules.println import println,inputln
from random import randint
import json

def RemoveSpaces(string):
    return ''.join([i for i in string if i != " "])

def GetAccounts():
    with open("Accounts.json","r") as file:
        try:
            accounts = json.load(file)
            return accounts
        except json.JSONDecodeError:
            return {}

ExistingAccounts = GetAccounts()
UserList = []

# these 2 constants are used for encryption, when we generate a random number we want it to be 32-bit so that it doesnt exceed unicode bits

LOWERBOUND = 0
UPPERBOUND = 65535

# we will add encryption later tho

def ShowPasswordRequirements():
    println("1. bigger than 8 characters")
    print("2. has special characters (!\"£$%^&*())\\")
    print("3. has both uppercase and lowercase letters")
    print("4. has digits in the password")

def ShowUsernameRequirements():
    println("1. has more than 2 characters")
    print("2. has both uppercase and lowercase letters")

def ValidatePassword(Password):
    if len(Password) < 8:
        return False
    HasPunc,HasDigits,HasUpper,HasLower = False,False,False,False
    for i in punctuation:
        if i in Password:
            HasPunc = True
            break
    for i in digits:
        if i in Password:
            HasDigits = True
            break
    for i in ascii_uppercase:
        if i in Password:
            HasUpper = True
            break
    for i in ascii_lowercase:
        if i in Password:
            HasLower = True
            break
    
    return ((HasPunc & HasLower) & (HasUpper & HasDigits))

def IsValidUsername(Username):
    HasLower,HasUpper = False,False
    if len(Username) < 2:
        return False
    for i in ascii_uppercase:
        if i in Username:
            HasUpper = True
            break
    for i in ascii_lowercase:
        if i in Username:
            HasLower = True
            break
    return HasLower & HasUpper
    

class User:
    def __init__(self,UserName,Password,Games={}):
        if not ValidatePassword(Password):
            println("Account was not created because of an invalid password")
            return
        self.UserName = UserName
        self.Password = Password
        self.Games = Games
    
    def AuthoriseUser(self):
        AttemptsLeft = 3
        while True:
            ConfirmationPassword = inputln("enter your password: ")
            while ConfirmationPassword != self.Password:
                AttemptsLeft -= 1
                if AttemptsLeft == 0:
                    println("You ran out of attempts to get the password correct, you cannot change your password now")
                    return False
                ConfirmationPassword = inputln(f"you entered an incorrect password, you now have {AttemptsLeft} tries to get it right, try again: ")
            return True
        
    def DeleteAccount(self):
        if self.AuthoriseUser(self):
            println("Account succesfully deleted")
            del self
            del ExistingAccounts[self.UserName]
        else:
            println("Account deletion failed due to unauthorised access to the account")
            return


    def ChangePassword(self):
        AttemptsLeft = 3

        if self.AuthoriseUser() == False:
            return 
        
        NewPassword = inputln("enter your new password: ")
        AttemptsLeft = 3
        while ValidatePassword(NewPassword) ==  False:
            println("your password has not been accepted, please make sure that your password is")
            ShowPasswordRequirements()
            NewPassword = inputln("enter your new password: ")

        self.Password = NewPassword

def CreateAccount():
    global ExistingAccounts

    println("DISCLAIMER! usernames and passwords must not have any spaces in them")

    def GettingUsername():
        Username = inputln("enter the username of this new account: ")

        while not IsValidUsername(Username):
            println("invalid username, make sure your username follows these requirements")
            ShowUsernameRequirements()
            Username = inputln("enter the username of this new account: ")
    
        if Username in ExistingAccounts.keys():
            println("Username already in use, try another username")
            return GettingUsername()
        
        println("ALERT! IF YOUR USERNAME HAS ANY SPACES IN IT, IT HAS BEEN REMOVED!")
        
        return RemoveSpaces(Username)
        
    def GettingPassword():
        Password = inputln("enter the Password of this new account: ")
        
        while not ValidatePassword(Password):
            println("invalid Password, make sure your Password follows these requirements")
            ShowPasswordRequirements()
            Password = inputln("enter the Password of this new account: ")
        
        if Password in ExistingAccounts.values():
            println("password already in use, try another password")
            return GettingPassword()
        
        println("ALERT! IF YOUR PASSWORD HAS ANY SPACES IN IT, IT HAS BEEN REMOVED!")

        return RemoveSpaces(Password)
    
    AccountUsername = GettingUsername()
    AccountPassword = GettingPassword()

    ExistingAccounts[AccountUsername] = AccountPassword

    with open("Accounts.json","w") as file:
        json.dump(ExistingAccounts,file,indent=4)
    
    ExistingAccounts = GetAccounts()