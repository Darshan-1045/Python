# this is a simple calculator Program

def add(a,b):
  return a+b

def sub(a,b):
  return a-b

def mul(a,b):
  return a*b

def div(a,b):
  return a/b

while True:

  print("This is a simple calculator")
  print("Select operation to perform")
  print("1. Addition")
  print("2. Substraction")
  print("3. Multiplication")
  print("4. Division")
  print("5. Exit")  

  choice = int(input("Enter your choice: "))

  if choice in {1,2,3,4} :
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

  if choice == 1:
    print("The sum is: ",add(a,b),)
    print("  ")

  elif choice == 2:
    print("The difference is: ",sub(a,b))
    print("  ")

  elif choice == 3:
    print("The product is: ",mul(a,b))
    print("  ")

  elif choice == 4:
    print("The quotient is: ",div(a,b))
    print("  ")

  elif choice == 5:
    print("Exiting the calculator. Goodbye!")
    break

  else:
    print("Invalid choice. Please try again.")
    print("  ")
