def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

def calculator():
    print("select type of operation")
    print("1. add")
    print("2. subtract")
    print("3. multiply")
    print("4. divide")
    choice = input("Enter choice (1/2/3/4): ")

    num1 = float(input("enter first number: "))
    num2 = float(input("enter the second number: "))
    
    if choice == "1":
        print(add(num1, num2))
    elif choice == "2":
        print(sub(num1, num2))
    elif choice == "3":
        print(multiply(num1, num2))
    elif choice == "4":
        print(divide(num1, num2))
    else:
        print("invalid message")

calculator()

