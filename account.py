# Balance Function
def show_balance(balance):
    print("Your current balance is: ", balance)

# Deposit Function
def deposit(balance):
    amount = float(input("Enter amount to deposit: "))
    balance += amount
    print("Deposit successful. New balance is: ", balance)
    return balance

# Withdraw Function
def withdraw(balance):
    while True:
        withdraw_amount = input("Enter amount to withdraw: ")
        if not withdraw_amount.isdigit():
            print("Error! Enter a valid amount")
            continue
        withdraw_amount = int(withdraw_amount)
        if withdraw_amount <= balance:
            balance -= withdraw_amount
            print("Withdrawal successful!")
            break
        else:
            print("Error! Insufficient funds")
    return balance

# Logout Function
def logout(name):
    print("Goodbye " + name + "!")