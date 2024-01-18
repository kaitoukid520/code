inventory = {}

def add_item(item, quantity):
    # Check if the item exists in the inventory dictionary.
    if item in inventory:
        # If it does, increase its quantity.
        inventory[item] += quantity
    else:
        # If not, add the item to the inventory with the given quantity.
        inventory[item] = quantity

    print(f"{quantity} {item}(s) added to the inventory.")

def view_inventory():
    # Loop through the inventory dictionary.
    print("\nCurrent Inventory:")
    for item, quantity in inventory.items():
        # Print each item's name and its quantity.
        print(f"{item}: {quantity}")

def update_item(item, quantity):
    # Check if the item exists in the inventory.
    if item in inventory:
        # If it does, update its quantity.
        inventory[item] = quantity
        print(f"{item}'s quantity updated to {quantity}.")
    else:
        # If the item doesn't exist, print a message indicating it's not found.
        print(f"Error: {item} not found in the inventory.")

def manage_inventory():
    while True:
        print("Inventory Management System")
        print("1. Add Item")
        print("2. View Inventory")
        print("3. Update Item Quantity")
        print("4. Exit")
        choice = input("Enter choice (1/2/3/4): ")

        # Process the user's choice
        if choice == '1':
            item = input("Enter item name: ")
            quantity = int(input("Enter quantity: "))
            add_item(item, quantity)
        elif choice == '2':
            view_inventory()
        elif choice == '3':
            item = input("Enter item name: ")
            quantity = int(input("Enter new quantity: "))
            update_item(item, quantity)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please enter a valid option (1/2/3/4).")
