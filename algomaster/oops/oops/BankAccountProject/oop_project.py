from bank_account  import *

Dave = BankAccount(1000, "Dave")
Sara = BankAccount(3000, "Sara Mathews")

Dave.getBalance()
Sara.getBalance() 

Sara.deposit(1500)

Dave.withdraw(500)
Sara.withdraw(5000)