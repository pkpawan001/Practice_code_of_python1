class Account:
    def __init__(self):
        self.bank_name = "Bank of India"
        self.account_holder_name = "Pawan Singh"
        self.account_num = "44541011008509"
        self.branch = "Supauli"
        self.balance = 100

    def details(self):
        print("Bank Name:", self.bank_name)
        print("Account Holder Name:", self.account_holder_name)
        print("Account Number:", self.account_num)
        print("Branch:", self.branch)
        print("Balance:", self.balance)

    def withdrawal(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print("Money debited. Your available balance is:", self.balance)
        else:
            print("Insufficient funds.")

    def check_balance(self):
        print("Available balance is:", self.balance)

    def deposit(self, amount):
            self.balance += amount
            print("Amount deposited. Your new balance is:", self.balance)
        

# instance of Account
A1 = Account()
A1.details()
A1.check_balance()
A1.deposit(100)
A1.withdrawal(11)


        

