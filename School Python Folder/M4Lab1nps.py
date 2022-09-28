print("Welcome to your Calculator program")

def add(x, y):
   return x + y

def subtract(x, y):
   return x - y

def multiply(x, y):
   return x * y

def divide(x, y):
   return x / y

choice = ["+", "-", "*", "/"]
keep_going = ["y", "n"]

while keep_going != "n":
    num1 = float(input("Enter first number: "))
    choice = input("What kind of calculation? Choose one of: +, -, *, /  ")
    num2 = float(input("Enter second number: "))

    if choice =="+":
        print(num1, choice, num2,"=", add(num1,num2))
    elif choice =="-":
        print(num1, choice, num2,"=", subtract(num1,num2))
    elif choice =="*":
        print(num1, choice, num2,"=", multiply(num1,num2)) 
    elif choice =="/":
        print(num1, choice, num2,"=", divide(num1,num2))
    else:
        print("invalid input")
    
    keep_going = input("Calculate? y or n? ")    
print("Closing the calculator.")