
import os

# Funksie om n produk en sy prys by die lys te voeg
def add_product(products):
    name = input("Enter product name: ")
    price = float(input("Enter product price: R"))
    products.append([name, price])

# Funksie om alle produkte en die totaal te bereken
def show_products(products):
    total = 0

    for product in products:
        print(product[0], "R{:.2f}".format(product[1]))
        total += product[1]

    print("Total R{:.2f}".format(total))

# Function to clear the CMD screen
def clear_screen():
    os.system("cls")

# Lys om alle produkte te stoor
products = []

# Sentinel variable
running = True


while running:
    # choose
    choice = input("Enter add, show, clear or exit: ")

    # Add a product
    if choice == "add":
        try:
            add_product(products)
        except ValueError:
            print("Invalid price")

    # Display all products
    elif choice == "show":
        show_products(products)

    # Clear the screen
    elif choice == "clear":
        clear_screen()

    # Exit the program 
    elif choice == "exit":
        running = False

    # Display an error for an invalid command
    else:
        print("Invalid choice")
