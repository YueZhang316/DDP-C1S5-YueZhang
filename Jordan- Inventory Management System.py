# Inventory Management System

# The inventory is stored in a dictionary.
# Keys are item names and values are quantities.
inventory = {}
    

# Function to add an item to the inventory
def add_item(item, quantity):
    if item in inventory:
        inventory[item] += quantity
    else:
        inventory[item] = quantity

# Function to view all items in the inventory
def view_inventory():
    for item, quantity in inventory.items():
        print(f"{item} : {quantity}")

# Function to update the quantity of an existing item in the inventory
def update_item(item, quantity):
    if item in inventory:
        inventory[item] = quantity
        print(f"Updated{item} : {quantity}")
    else:
        print(f"Error: Item '{item}' not found in the inventory.")

# Main function to manage the inventory
def manage_inventory():
    while True:
        print("\nInventory Management System")
        print("1. Add Item")
        print("2. View Inventory")
        print("3. Update Item Quantity")
        print("4. Exit")
        choice = input("Enter choice (1/2/3/4): ")

        # Process the user's choice
        if choice == "1":
            item = input("Enter item name: ").upper()
            quantity = int(input("Enter quantity: "))
            add_item(item, quantity)
        elif choice == "2":
            view_inventory()
        elif choice == '3':
            item = input("Enter item: ")
            quantity = int(input("Enter new quantity: "))
            update_item(item, quantity)
        elif choice == '4':
            print("Exitng program...")
            break
        else:
            print("Error: Invalid choice. Please enter a valid option (1/2/3/4).")

# Entry point of the program
manage_inventory()