class account :
  def __init__ (self,balance):
    self.__balance = balance

  def deposit(self,amount):
    self.__balance += amount 
    print(f"Deposited {amount}. New balance: {self.__balance}")

  def withdraw(self,amount):
    if amount <= self.__balance:
      self.__balance -= amount
      print(f"Withdrew {amount}. New balance: {self.__balance}")
    else: 
      print("Insufficient balance")

  def balance(self):
    print(f"Current Balance: {self.__balance}")


acc1 = account(10000)

acc1.deposit(4000)
acc1.withdraw(2000)

acc1.balance()
