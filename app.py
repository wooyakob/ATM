# Import the Banking Packing
from banking_pkg import account

# ATM Function
def atm_menu(name):
    print("")
    print("          === Automated Teller Machine ===          ")
    print("User: " + name)
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")


# Account Registration
print("          === Automated Teller Machine ===          ")

# Bonus While Loop / Limit User Name Length

while True:
    name = input("Enter name to register (1-10 characters): ")
    if len(name) > 0 and len(name) <= 10:
        break
    else:
        print("Error! Enter a name between 1 - 10 characters")

# Bonus While Loop / Limit User Pin Length
while True:
    pin = input("Enter PIN (1 - 4 characters): ")
    if not (len(pin) == 4):
        print("Error! Enter a pin between 1 - 4 characters")
    else:
        break

balance = 0

print(name + " has been registered with a starting balance of " + str(balance))

# Log in screen
print("\n          === Automated Teller Machine ===          ")
print("LOGIN")
print("Enter name: " + name)
print("Enter PIN: " + pin)
print("Login successful! \n")

# Name and Pin Validation While Loop
while True:
    name_to_validate = input("Enter name: ")
    pin_to_validate = input("Enter PIN: ")
    if name_to_validate == name and pin_to_validate == pin:
        print("Login successful!")
        break
    else:
        print("Invalid credentials \n")
        continue

# Balance Logic While Loop
while True:
    atm_menu(name)
    option = input("Choose an option: ")
    if option == "1":
        account.show_balance(balance)
    elif option == "2":
        balance = account.deposit(balance)
        account.show_balance(balance)
    elif option == "3":
        balance = account.withdraw(balance)
        account.show_balance(balance)
    elif option == "4":
        account.logout(name)
        break
    else:
        print("Invalid option, please try again")