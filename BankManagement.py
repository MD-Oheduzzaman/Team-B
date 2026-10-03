class BankAccount:
    def __init__(self,name,id,accountnumber=0,balance=0):
        self.name=name
        self.accountnumber=accountnumber
        self.balance=balance
        self.id = id

    def deposit(self,amount):
        self.balance+=amount
    def AccountStatus(self):
        print("Account Name: ",self.name)
        print("Account ID: ",self.id)
        print("Account Number: ",self.accountnumber)  
        print("Balance: ",self.balance) 
        
    def withdrawMoney(self,amount):
        self.balance=self.balance-amount



account_initial = 1000
accounts = {}
while True:
    print("\n................Team_B Bank Ltd.................")
    print("1. Create Accout")
    print("2. Check Status")
    print("3. Deposit")
    print("4. Withdraw ")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    match choice:
        case 1:
            name = input("Enter your name")
            id = input("Enter your ID: ")
            balance = 0
            accountnumber = account_initial+1
            account = BankAccount(name,id,accountnumber,balance)
            accounts[accountnumber] = account
            print("Accounnt Succesfully created")
            print("Your Account Number: ",account.accountnumber)
            account_initial+=1
        case 2:
            account_number = int(input("Enter your Account Number: "))
            if account_number in accounts:
                account = accounts[account_number]
                account.AccountStatus()
            else: 
                print("Account Not found5")
        case 3:
            account_number = int(input("Enter your Account Number: "))
            if account_number in accounts:
                amount = int(input("Enter Deposit Amount: "))
                account = accounts[account_number]
                account.deposit(amount)
                print("Deposit successful!")
                print("New balance:", account.balance)
            else:
                print("account not found")
        case 4:
            account_number = int(input("Enter your account Number: "))
            if account_number in accounts:
                amount = int(input("enter withdraw amount: "))
                account.withdrawMoney(amount)
                print("Money Withraw Succesfull")
                print("New balance:", account.balance)
            else:
                print("Account Not Found")
        case 5:
            print("Thank you for using Team_B Bank Ltd")
            break
        case _:
            print("Invalid chaoice")
