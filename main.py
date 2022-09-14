
class WafiAccount:
    """ Wafi-Cash peer to peer payment app"""
    '''
    def __init__ (self, account_name, account_balance):
        self.account_name = account_name
        self.account_balance = account_balance
        print('Wafi-Cash Account for customer, ' + self.account_name)
    '''

    def __init__(self, account_name, account_balance={"USD": 20, "NGN" : 20, "GBP":20, "YUAN": 20}):
        self.account_name = account_name
        self.account_balance=account_balance
        print('Wafi-Cash Account for customer, ' + self.account_name)
    
    # Deposit to Wafi-Cash Account
    def deposit(self, currency, amount):
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
        return self.account_balance

    def currency_conversion(self, currency, other_currency, amount):
        rate = { "USD": 1, "NGN" : 415, "GBP":0.86, "YUAN" : 6.89}
        if currency == "USD":
            amount = amount/rate[other_currency]
        elif currency == "GBP":
            amount =(amount/rate[other_currency])*rate["GBP"]
        elif currency == "YUAN":
            amount = (amount/rate[other_currency])*rate["YUAN"]
        return amount

    # Funds Transfer from  Wafi-Cash Account
    def transfer(self, currency, amount, account_name):

        if self.account_balance[currency] > amount:
            self.account_balance[currency] = self.account_balance[currency] - amount
            account_name.account_balance[currency] = account_name.account_balance[currency] + amount
            print("Hello, you transferred: {}".format(amount))
        
