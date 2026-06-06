class Bank:
    def openAccount(self,acno,cname,balance):
        self.acno=acno
        self.cname=cname
        self.balance=balance
        print("Hello ",cname," , Your Account Number ",acno," Is Opened With ",balance," Rs.")

    def deposit(self,amount):
        self.balance=self.balance+amount

    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance=self.balance-amount
        else:
            print("Sorry You Need Another ",amount-self.balance," Rs.")

    def checkBalance(self):
        print("Your Current Balance Is : ",self.balance)

b1=Bank()

b1.openAccount(101,"Bipin Maurya",1000)

while True:
    print("*"*50)
    print("1. Deposit")
    print("2. Withdrawal")
    print("3. Check Balance")
    print("4. Exit")
    print("*"*50)

    choice=int(input("Enter Your choice : "))

    if choice==1:
        amount=int(input("Enter Deposit Amount : "))
        b1.deposit(amount)
    elif choice==2:
        amount=int(input("Enter Withdrawal Amount : "))
        b1.withdraw(amount)
    elif choice==3:
        b1.checkBalance()
    elif choice==4:
        print("Thank you your services")
        break
    else:
        print("Invalid Your Number")
