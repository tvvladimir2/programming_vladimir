# Store data to disk

import pickle # default python module
import os # clear the screen

os.system('cls') # Clear the screen on Windows

account = pickle.load(open("account1.dat", "rb")) # Load account1.dat file with stored values #rb=read binary
if type(account) == int: # Checking is var<account> is already created and equals integer
    print("Account found")
else:
    # Create the account if the account is not created
    print("Account is not created")
    print("How much money would you like to put in? Type an amount:")
    account = input("> ")
    print("Creating a new account for Grigory")
    pickle.dump(account, open("account1.dat", "wb")) # wb=write binary
    # pickle.dump(account, open("account1.dat", "wb"))

#Create a function for adding money to var<account>
def add():
    print("\n"*3)
    global account
    print("How much do you want to add (+) ? ")
    add = int(input("> "))
    account = account + add
    print("You have been successfully added " + str(add) + " Eur to your account"+"\n"*3)

#Create a function for substracting money from var<account>
def substract():
    print("\n"*3)
    global account
    print("How much do you want to substract (-) ? ")
    substract = int(input("> "))
    account = account - substract
    print("You have been successfully substracted " + str(substract) + " Eur from your account"+"\n"*3)

#Create a function for showing additional information
def advice():
    print("\n"*3)
    print("You can save money to buy the following items:")
    print("1) A kayak! You will be able to paddle with your dad!")
    print("2) A virtual reality headset! Play those awesome games or model in Blender in 3d environment!")
    print("3) If you still didn't decide, don't spend it all now, ideas will come!")
    print("\n")
    print("Press any key to go back to menu.")
    input()

#Main loop with simple options to choose from
while True:
    print("This is Grigory's home bank account.")
    print("Currently you have: " + str(account) + " Eur.")
    print('''Please choose action "1", "2", or "3": ''')
    print("1) Add money to the account")
    print("2) Substract money from the account")
    print("3) Close the application")
    print("4) Word of advice")
    action = input(">") #varible for choice of action
    if action == "1":
        add()
        pickle.dump(account, open("account1.dat", "wb"))
    if action == "2":
        substract()
        pickle.dump(account, open("account1.dat", "wb"))
    if action == "3":
        break
    if action == "4":
        advice()
