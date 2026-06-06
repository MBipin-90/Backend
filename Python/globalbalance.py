def deposit(amount):
    global balance
    balance=10000
    balance+=amount

def withdraw(amount):

    if amount <= balance:
        balance=balance-amount

deposit(5000)
withdraw(1000)


print(balance)
