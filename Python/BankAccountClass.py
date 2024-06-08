class BankAccount:
    def __init__(self,account_number, account_holder, balance):
        self.account_number = account_number
        self.account_holder = account_holder 
        self.balance = balance 
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        if(self.balance >= amount):
            self.balance -= amount
            return(True)
        else:
            return(False)
    def get_balance(self):
        return(self.balance)

account_number = input() 
account_holder = input() 
balance = 0.0
bank_acc = BankAccount(account_number, account_holder, balance)
deposit_amount = int(input())
bank_acc.deposit(deposit_amount)
withdraw_amount = int(input())
withdraw_result = bank_acc.withdraw(withdraw_amount)
print(withdraw_result)
balance_result = bank_acc.get_balance() 
print(balance_result)