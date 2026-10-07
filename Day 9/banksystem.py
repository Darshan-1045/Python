class Account :
  def __init__(self,accNumber,HolderName):
    self.accNUmber = accNumber
    self.HolderName = HolderName
    self._Balance = 0

  def deposit(self,amount): 
    self._Balance += amount
    print(f"Deposited {amount}.  balance : {self._Balance}")

  def withdraw(self,amount):
    if amount > self._Balance:
      print("Insufficient balance")
    else:
      self._Balance -= amount
      print(f"Withdrawn {amount}.  balance : {self._Balance}")

  def getBalance(self):
    return self._Balance

  

class savingsAccount(Account):
 
  def calculateInterest(self):
    rate = 0.2
    interest = self._Balance * rate / 100
    self._Balance += interest
    print(f"Interest of {interest} added. New balance: {self._Balance}")
  

class currentAccount(Account):
  def withdraw(self,amount):
    overdraft_limit = 1000
    if amount > self._Balance + overdraft_limit:
      print("Insufficient balance and overdraft limit exceeded")
    else:
      self._Balance -= amount
      print(f"Withdrawn {amount}.  balance : {self._Balance}")

class Bank:
  def __init__(self,name,city):
    self.name = name
    self.city = city
    self.__accounts = {}

  def createAccount(self,accNumber,HolderName,accountType):
    if accNumber in self.__accounts:
      print("Account number already exists")
      return None
    
    if accountType == "savings":
      account = savingsAccount(accNumber,HolderName)
    elif accountType == "current":
      account = currentAccount(accNumber,HolderName)
    else:
      print("Invalid account type")
      return
    self.__accounts[accNumber] = account
    print(f"Account created for {HolderName} with account number {accNumber}")

    return account  

  def getAccount(self,accNumber):
    if accNumber in self.__accounts:
      return self.__accounts[accNumber]
    else:
      print("Account not found")
      return None
  
  
bank = Bank("MyBank","New York")

a1 = bank.createAccount(12345,"John Doe","savings")
a2 = bank.createAccount(67890,"Jane Smith","current")

a1.deposit(1000)
a1.calculateInterest()

a2.deposit(500)
a2.withdraw(600)

  