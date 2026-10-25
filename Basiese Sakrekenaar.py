import os

# Addition function
def plus(a, b):
    return a + b

# Subtraction function
def minus(a, b):
    return a - b

# Multiplication functin
def multiply(a, b):
    return a * b

# Division function
def divide(a, b):
    return a / b

# Sentinel variable
running = True

while running:
    # choose
    choice = input("Enter +, -, *, /, clear or exit: ")

    # Exit
    if choice == "exit":
        running = False

    # Clear
    elif choice == "clear":
        os.system("cls")

    # calculation
    elif choice in ["+", "-", "*", "/"]:
        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))

            if choice == "+":
                print(plus(a, b))

            elif choice == "-":
                print(minus(a, b))

            elif choice == "*":
                print(multiply(a, b))

            elif choice == "/":
                print(divide(a, b))

        except ValueError:
            print("Invalid number")

    else:
        print("Invalid choice")