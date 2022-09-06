class WafiAccount:
    """simple account balance of bank"""
    def __init__ (self, account_name, account_balance):
        self.account_name = account_name
        self.account_balance = account_balance
        print('Wafi-Cash Account for customer, ' + self.account_name)

    # Deposit to Wafi-Cash Account
    def deposit(self, amount):
        if amount > 0:
            self.account_balance += amount
            self.account_statement()

    # Withdrawal from Wafi-Cash Account
    def withdraw(self, amount):
        if amount > 0 and self.account_balance > amount:
            self.account_balance -= amount
            self.account_statement()
        else:
            print("The Amount in your Wafi-Cash Account Balance is not Sufficent")
            self.account_statement()

    # Check  Wafi-Cash Account Balance
    def account_statement(self):
        print("Hello {} Your  Wafi-Cash Account Balance is {}".format(self.account_name, self.account_balance))

    # Funds Transfer from  Wafi-Cash Account
    def transfer(self, amount, account_name):
        self.account_balance = self.account_balance - amount
        account_name.account_balance = account_name.account_balance + amount
        print("Hello, you transferred: {}".format(amount))
