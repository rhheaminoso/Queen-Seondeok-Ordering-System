print("======================================")
print("          QUEEN SEONDEOK")
print("          ORDERING SYSTEM")
print("======================================")

# STAFF LOGIN
login = False

while login == False:
    username = input("Enter staff username: ")
    password = input("Enter staff password: ")

    if username == "samg" and password == "1234":
        print("\nLogin Successful!")
        print("Welcome to QUEEN SEONDEOK!")
        login = True
    else:
        print("\nLogin Failed!")
        print("Invalid username or password.")
        print("Please try again.\n")

# CUSTOMER TABLE
table = input("\nEnter customer table number: ")

# SET A MENU
set_a = [
    "Pork 1",
    "Pork 2",
    "Rice",
    "Kimchi",
    "Lettuce",
    "Sauce",
    "Drinks"
]

# SET B MENU
set_b = [
    "Pork 1",
    "Pork 2",
    "Pork 3",
    "Pork 4",
    "Cheese",
    "Rice",
    "Kimchi",
    "Lettuce",
    "Sauce",
    "Drinks"
]

price_a = 199
price_b = 245

# DISPLAY MENU
print("\n========== SAMGYUPSAL MENU ==========")
print("\n1. Set A - PHP 199")
print("Inclusions:")

for item in set_a:
    print("-", item)

print("\n2. Set B - PHP 245")
print("Inclusions:")

for item in set_b:
    print("-", item)

print("\nNOTE: SAMGYUPSAL IS UNLIMITED!")
print("Refills are free of charge.")

# CHOOSE SET
choice = 0

while choice != 1 and choice != 2:
    try:
        choice = int(input("\nChoose your set (1 or 2): "))

        if choice != 1 and choice != 2:
            print("Invalid choice. Please select 1 or 2.")

    except:
        print("Invalid input. Please enter a number.")
        choice = 0

# SELECT SET DETAILS
if choice == 1:
    set_name = "Set A"
    price = price_a
    menu = set_a.copy()
else:
    set_name = "Set B"
    price = price_b
    menu = set_b.copy()

# DISPLAY SELECTED SET
print("\n======================================")
print("          SELECTED SET")
print("======================================")
print("Selected Set:", set_name)
print("Price: PHP", price)
print("\nSet Inclusions:")

for item in menu:
    print("-", item)

# CUSTOMIZE ORDER
print("\n======================================")
print("          CUSTOMIZE ORDER")
print("======================================")
print("Do you want to remove any item?")
print("Enter item numbers separated by commas.")
print("Example: 3,4")
print("Enter 0 if you want all items.")

for i in range(len(menu)):
    print(str(i + 1) + ".", menu[i])

# SELECT ITEMS TO REMOVE
remove_choices = []
valid_input = False

while valid_input == False:
    remove_input = input("\nItems to remove: ")

    try:
        numbers = remove_input.split(",")
        remove_choices = []

        for number in numbers:
            remove_choices.append(int(number.strip()))

        if remove_choices == [0]:
            remove_choices = []
            valid_input = True

        elif 0 in remove_choices:
            print("Enter 0 alone to keep all items.")

        else:
            valid = True

            for number in remove_choices:
                if number < 1 or number > len(menu):
                    valid = False

            if valid == True:
                valid_input = True
            else:
                print("Invalid item number. Please try again.")

    except:
        print("Invalid input. Please enter item numbers.")

# IDENTIFY REMOVED ITEMS
removed_items = []

for number in remove_choices:
    item = menu[number - 1]

    if item not in removed_items:
        removed_items.append(item)

# IDENTIFY INCLUDED ITEMS
ordered_items = []

for item in menu:
    if item not in removed_items:
        ordered_items.append(item)

# DISPLAY CUSTOMIZED ORDER
print("\n======================================")
print("          CUSTOMIZED ORDER")
print("======================================")
print("Selected Set:", set_name)

print("\nIncluded Items:")

for item in ordered_items:
    print("-", item)

print("\nRemoved Items:")

if len(removed_items) > 0:
    for item in removed_items:
        print("-", item)
else:
    print("None")

print("\nSet price remains unchanged.")

# ENTER QUANTITY
quantity = 0

while quantity <= 0:
    try:
        quantity = int(input("\nEnter quantity of sets: "))

        if quantity <= 0:
            print("Quantity must be at least 1.")

    except:
        print("Invalid input. Please enter a number.")
        quantity = 0

# CALCULATE SUBTOTAL
subtotal = price * quantity

# REFILL MENU
refill_items = ordered_items.copy()
refill_orders = []

# ORDER CONFIRMATION
print("\n======================================")
print("       ORDER ADDED SUCCESSFULLY!")
print("======================================")
print("Table Number:", table)
print("Selected Set:", set_name)
print("Quantity:", quantity)
print("Price per Set: PHP", format(price, ".2f"))
print("Subtotal: PHP", format(subtotal, ".2f"))
print("Thank you for choosing QUEEN SEONDEOK!")

# UNLIMITED REFILL SYSTEM
another = "yes"

while another != "no":

    another = input(
        "\nWould you like a refill? (yes/no): "
    ).lower().strip()

    if another == "yes":

        print("\n========== AVAILABLE REFILLS ==========")

        for i in range(len(refill_items)):
            print(str(i + 1) + ".", refill_items[i])

        print("0. Cancel refill")

        # CHOOSE REFILL ITEMS
        refill_valid = False
        refill_choices = []

        while refill_valid == False:
            refill_input = input(
                "\nChoose items to refill (e.g., 1,2): "
            )

            try:
                numbers = refill_input.split(",")
                refill_choices = []

                for number in numbers:
                    refill_choices.append(int(number.strip()))

                if refill_choices == [0]:
                    refill_choices = []
                    refill_valid = True

                elif 0 in refill_choices:
                    print("Enter 0 alone to cancel.")

                else:
                    valid = True

                    for number in refill_choices:
                        if number < 1 or number > len(refill_items):
                            valid = False

                    if valid == True:
                        refill_valid = True
                    else:
                        print("Invalid item number.")

            except:
                print("Please enter valid item numbers.")

        # ADD REFILL ORDERS
        if len(refill_choices) == 0:
            print("Refill cancelled.")

        else:
            print("\n======================================")
            print("       REFILL ADDED SUCCESSFULLY!")
            print("======================================")

            for number in refill_choices:
                item = refill_items[number - 1]
                refill_orders.append(item)
                print("-", item)

            print("Additional Charge: PHP 0.00")
            print("======================================")

    elif another == "no":
        print("\nThank you! Your order is complete.")

    else:
        print("Invalid answer. Please enter yes or no.")
        another = "yes"

# CALCULATE TOTAL
total = subtotal

# PRINT RECEIPT
print("\n======================================")
print("           QUEEN SEONDEOK")
print("                RECEIPT")
print("======================================")
print("Table Number:", table)
print("--------------------------------------")
print("Selected Set:", set_name)
print("Quantity:", quantity)
print("Price per Set: PHP", format(price, ".2f"))
print("Subtotal: PHP", format(subtotal, ".2f"))

# PRINT SET INCLUSIONS
print("\nCUSTOMIZED SET INCLUSIONS:")

for item in ordered_items:
    print("-", item)

# PRINT REMOVED ITEMS
print("\nREMOVED ITEMS:")

if len(removed_items) > 0:
    for item in removed_items:
        print("-", item)
else:
    print("None")

# PRINT REFILL ORDERS
print("\nREFILL ORDERS:")

if len(refill_orders) > 0:
    for i in range(len(refill_orders)):
        print(str(i + 1) + ".", refill_orders[i])

    print("Total Refill Items:", len(refill_orders))
else:
    print("No refills requested.")

print("Refill Charges: PHP 0.00")

# FINAL PAYMENT
print("--------------------------------------")
print("TOTAL PAYMENT: PHP", format(total, ".2f"))
print("======================================")
print("       THANK YOU FOR DINING!")
print("          QUEEN SEONDEOK")
print("======================================")
