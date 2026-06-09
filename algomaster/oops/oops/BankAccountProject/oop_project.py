from bank_account  import *

Dave = BankAccount(1000, "Dave")
Sara = BankAccount(3000, "Sara Mathews")

Dave.getBalance()
Sara.getBalance() 

Sara.deposit(1500)

Dave.withdraw(500)
Sara.withdraw(5000)

Dave.transfer(200, Sara)
Sara.transfer(5000, Dave)

Jim = InterestRewardAccount(2000, "Jim")
Jim.getBalance()
Jim.deposit(1000)

Jim.transfer(500, Dave)  

Blaze = SavingsAccount(1500, "Blaze")
Blaze.getBalance()
Blaze.deposit(500)
Blaze.transfer(700, Jim)
Blaze.withdraw(300)