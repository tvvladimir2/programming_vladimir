import pickle # default python module for saving data to disk
import os # clear the screen

os.system('cls') # Clear the screen on Windows

# account = 100
# pickle.dump(account, open("account.dat", "wb"))

account = pickle.load(open("account.dat", "rb")) # Load account.dat file with stored values #rb=read binary
print (hex(account))
if type(account) == int: # Checking is var<account> is already created and equals integer
    print("Account found")
else:
    # Create the account if the account is not created
    print("Account is not created")
    print("How much money would you like to put in? Type an amount:")
    account = input("> ")
    print("Creating a new account for Grigory")
    pickle.dump(account, open("account.dat", "wb")) # wb=write binary
    # pickle.dump(account, open("account.dat", "wb"))

def add():
    print("\n"*2)
    global account
    print("How much do you want to add?")
    choice=int(input("> "))
    account += choice
    print("You have added " + str(choice) + " Eur.")

def zero():
    print("\n"*2)
    global account
    account -= account

def subtract():
    print("\n"*2)
    print("How much do you want to subtract?")
    choice=input("> ")
    account -= choice

def divide():
    print("\n"*2)
    print("How much do you want to divide?")
    choice=input("> ")
    account /= choice

while True:
    print("\n"*2)
    print("This is grigory's account")
    print("Grigory Tazev has "+str(account) + " Eur.")
    print ("Binary number: "+ hex(account))
    print("Hello. what would you like to do?")
    print("1) add")
    print("2) subtract")
    print("3) divide")
    print("4) close program")
    print("5) Zero the account")
    choice = input(">")
    if choice == '1':
        add()
        pickle.dump(account, open("account.dat", "wb"))
    if choice == '2':
        subtract()
        pickle.dump(account, open("account.dat", "wb"))
    if choice == '3':
        divide()
        pickle.dump(account, open("account.dat", "wb"))
    if choice == '4':
        print("BURN IN HELL (: (closing)")
        break
    if choice == '5':
        zero()
        pickle.dump(account, open("account.dat", "wb"))
        print("Your account is now equal to 0")
        print("Boys don't cry")
