class BalanceException(Exception):
    pass
class BankAccount:
    def __init__(self,initialAmt, AccountHolderName):
        self.balance = initialAmt
        self.name =AccountHolderName
        print(f"Account created for '{self.name}' with initial balance of ${self.balance:.2f}")
        
    def getBalance(self):
        print(f"Account '{self.name}' balance = ${self.balance:.2f}")
        
    def deposit(self, amount):
        self.balance += amount
        print("\n Deposit Completed!")
        self.getBalance()
        
    def viableTransaction(self, amount):
        if self.balance >= amount:
            return 
        else:
            raise BalanceException(f"Transaction Failed! Insufficient Balance in account ")
    def withdraw(self, amount): 
        try:
            self.viableTransaction(amount)
            self.balance -= amount
            print("\n Withdrawal Completed!")
            self.getBalance()
            
        except BalanceException as error:
            print(f"\nBalance interrupted: {error}")
            