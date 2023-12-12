# Menu dictionary
menu = {
    "Snacks": {
        "Cookie": .99,
        "Banana": .69,
        "Apple": .49,
        "Granola bar": 1.99
    },
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    },
    "Drinks": {
        "Soda": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99
        },
        "Tea": {
            "Green": 2.49,
            "Thai iced": 3.99,
            "Irish breakfast": 2.49
        },
        "Coffee": {
            "Espresso": 2.99,
            "Flat white": 2.99,
            "Iced": 3.49
        }
    },
    "Dessert": {
        "Chocolate lava cake": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49
    }
}

# 1. Set up order list. Order list will store a list of dictionaries for
# menu item name, item price, and quantity ordered
#create an empty list
order_list = []
#add an item to the order list
def add_to_list(item_name, item_price, quantity):
    order_item = {
        'item_name': item_name,
        'item_price': item_price,
        'quantity': quantity
    }
    order_list.append(order_item)


# Launch the store and present a greeting to the customer

print("Welcome to the variety food truck.")
# Customers may want to order multiple items, so let's create a continuous
# loop
place_order = True
while place_order:
     # Ask the customer from which menu category they want to order
    print("From which menu would you like to order? ")
    # Create a variable for the menu item number
    i = 1
    # Create a dictionary to store the menu for later retrieval
    menu_items = {}
     # Print the options to choose from menu headings (all the first level
    # dictionary items in menu).
    for key in menu.keys():
        print(f"{i}: {key}")
        # Store the menu category associated with its menu item number
        menu_items[i] = key
        # Add 1 to the menu item number
        i += 1
    #Get the customer's input
    menu_category = input("Type menu number: ")
    #Check if the customer's input is a valid option
    if menu_category.isdigit():
        #Save the menu category name to a variable
        if int(menu_category) in menu_items.keys():
            menu_category_name = menu_items[int(menu_category)]
            #Print out the menu category name they selected
            print(f"You selected {menu_category_name}")
            #Print out the menu options from the menu_category_name
            print(f"What {menu_category_name} item would you like to order?")
            i = 1
            #Displaying items from the selected menu category
            menu_items = {}
            for key, value in menu[menu_category_name].items():
                if isinstance(value, dict):
                    for key2, value2 in value.items():
                        print(f"{i}: {key} - {key2} | ${value2}")
                        menu_items[i] = {"Item name": f"{key} - {key2}", "Price": value2}
                        i += 1
                else:
                    print(f"{i}: {key} | ${value}")
                    menu_items[i] = {"Item name": key, "Price": value}
                    i += 1
            #Getting customers choice for specific item
            item_choice = input("Please enter a menu item number or q to quit: ")
            if item_choice.lower() == 'q':
                break
            elif item_choice.isdigit() and int(item_choice) in menu_items.keys():
                item_choice_int = int(item_choice)
                selected_item = menu_items[item_choice_int]["Item name"]
                quantity_input = input(f"How many {selected_item} would you like? ")
                quantity = int(quantity_input) if quantity_input.isdigit() else 1
                add_to_list(selected_item, menu_items[item_choice_int]["Price"], quantity)
                print(f"You've added {quantity} {selected_item} to your order.")
        else:
            print("That was not a valid menu option.")
    else:
        print("You didn't select a number.")
    #Asking customer if they want to keep ordering
    keep_ordering = input("Would you like to keep ordering? (Y)es or (N)o ")
    if keep_ordering.upper() == 'N':
        place_order = False
        print("Thank you for your order!")

# Print out the customer's order
print("This is what we are preparing for you.\n")
print("Item name               | Price  | Quantity")
for order_item in order_list:
    item_name = order_item['item_name']
    item_price = order_item['item_price']
    quantity = order_item['quantity']
    num_item_spaces = 24 - len(item_name)
    item_spaces = " " * num_item_spaces
    price_str = f"${item_price}"
    price_spaces = " " * (8 - len(price_str))
    quantity_str = str(quantity)
    quantity_spaces = " " * (10 - len(quantity_str))
    print(f"{item_name}{item_spaces}|{price_str}{price_spaces}|{quantity_str}{quantity_spaces}")

# Calculate the total cost
total_cost = sum(item['item_price'] * item['quantity'] for item in order_list)
print("\nTotal Cost: $" + str(total_cost))
