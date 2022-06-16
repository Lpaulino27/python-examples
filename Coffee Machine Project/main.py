MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },

        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}


def show_report():
    """"Function to create the report view"""
    print("Water: " + str(resources["water"]) + "ml")
    print("Milk: " + str(resources["milk"]) + "ml")
    print("Coffee: " + str(resources["coffee"]) + "g")
    print("Money: $" + str(resources["money"]))


def check_resources(drink_selected):
    """To check the quantity of resources
    return True if it is possible to prepare a drink"""
    water_sel = int(MENU[drink_selected]["ingredients"]["water"])
    milk_sel = int(MENU[drink_selected]["ingredients"]["milk"])
    coffee_sel = int(MENU[drink_selected]["ingredients"]["coffee"])

    water_stock = int(resources["water"])
    milk_stock = int(resources["milk"])
    coffee_stock = int(resources["coffee"])

    if water_sel > water_stock:
        print("Sorry there is not enough water")
        return False
    elif milk_sel > milk_stock:
        print("Sorry there is not enough milk")
        return False
    elif coffee_sel > coffee_stock:
        print("Sorry there is not enough coffee")
        return False
    else:
        return True


def process_coins(drink_selected):
    """To ask the client for paying the drink"""
    # Getting the cost for the selected drink
    drink_cost = float(MENU[drink_selected]["cost"])

    # Looking for the coins inserted by the client
    print("Please insert coins.")
    quarters = float(input("How many quarters?:"))
    dimes = float(input("How many dimes?:"))
    nickles = float(input("How many nickles?:"))
    pennies = float(input("How many pennies?:"))

    # Calculating the total amount
    total = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)

    # Checking if there is enough money
    if total > drink_cost:
        change = round(total - drink_cost, 2)
        resources["money"] = float(resources["money"]) + drink_cost
        print(f"Here is ${change} dollars in change")
        return True
    elif total == drink_cost:
        resources["money"] = float(resources["money"]) + drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def prepare_drink(drink_selected):
    """"To prepare the drink selected"""
    water_sel = int(MENU[drink_selected]["ingredients"]["water"])
    milk_sel = int(MENU[drink_selected]["ingredients"]["milk"])
    coffee_sel = int(MENU[drink_selected]["ingredients"]["coffee"])

    # Updating stock
    resources["water"] = int(resources["water"]) - water_sel
    resources["milk"] = int(resources["milk"]) - milk_sel
    resources["coffee"] = int(resources["coffee"]) - coffee_sel

    # Showing final message
    print(f"Here ir your {drink_selected}. Enjoy!")


def start():
    """"Main function to the coffee machine"""
    order = input("What would you like? (espresso/latte/cappuccino):")

    while order.lower() != "off":
        if order.lower() == "espresso" or order.lower() == "latte" or order.lower() == "cappuccino":
            # Checking the resources availability
            if check_resources(order.lower()):
                # Checking the amount of money
                if process_coins(order.lower()):
                    # Preparing the drink
                    prepare_drink(order.lower())
        if order.lower() == "report":
            show_report()
        order = input("What would you like? (espresso/latte/cappuccino):")


start()