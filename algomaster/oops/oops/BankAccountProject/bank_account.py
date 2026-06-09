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
            
    def transfer(self, amount, account):
        try:
            print('\n***********\n\n Initiating Transfer...🚀')
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print(f"\n Transfer Completed!✅ ${amount:.2f} transferred from '{self.name}' to '{account.name}'\n\n***********")
            self.getBalance()
            account.getBalance()
        
        except BalanceException as error:
            print(f"\nBalance interrupted ❌: {error}")
            
class InterestRewardAccount(BankAccount):
    def deposit(self, amount):
        self.balance += amount*1.05 
        print("\n Deposit Completed with 5% Bonus!")
        self.getBalance()  
        
class SavingsAccount(InterestRewardAccount):
    def __init__(self, initialAmt, AccountHolderName):
        super().__init__(initialAmt, AccountHolderName)
        self.fee = 5
    
    def withdraw(self, amount):
        try:
            self.viableTransaction(amount +self.fee)
            self.balance -= (amount + self.fee)
            print(f"\nWithdrawal Completed with ${self.fee} fee!")
            self.getBalance()
        
        except BalanceException as error:
            print(f"\nBalance interrupted: {error}")
        