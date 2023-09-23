MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# TODO 4. Check resources sufficient?And checking what the user enters(coffee choice) by creating function


def check_resources(ingredients, resources):
    sufficient_resources = True
    # Iterate over the ingredients
    for ingredient in ingredients:
        # Check if the required amount of ingredient is available in resources
        if resources[ingredient] < ingredients[ingredient]:
            # If not enough, print a message
            print(f"Sorry there is not enough  {ingredient}.")
            sufficient_resources = False

    if sufficient_resources:
        # If enough, subtract the required amount from the resources
        resources["water"] -= ingredients["water"]
        resources["coffee"] -= ingredients["coffee"]

    return sufficient_resources



def user_selection(user_input, MENU):
    ingredients = MENU[user_input]["ingredients"]
    return check_resources(ingredients, resources)


maintenance = False

while not maintenance:
    user_input = input("What would you like? (espresso/latte/cappuccino): ")
    # TODO 2. Turn off the Coffee Machine by entering “off” to the prompt
    if user_input == 'off':
        print("Maintenance Mood")
        maintenance = True
    # TODO 3.  Print report and what the user select.
    elif user_input == 'report':
        print(f"Water:{resources['water']}ml\nMilk {resources['milk']}ml\nCoffe:{resources['coffee']}g\nCost:{profit}$")
    else:
        sufficient_resources = user_selection(user_input, MENU)

        # TODO 5. ask user to enter Money(coins)
        if sufficient_resources:
            print("Please insert coins.")
            Quarters = int(input("How many quarters?: ")) * 0.25
            Dimes = int(input("How many dimes?: ")) * 0.1
            Nickles = int(input("How many nickles?:  ")) * 0.05
            Pennies = int(input("How many pennies?: ")) * 0.01
            Total = Quarters + Dimes + Nickles + Pennies  # Calculate the total amount of coins
            if Total >= MENU[user_input]["cost"]:
                Cost = Total - MENU[user_input]["cost"]  # Subtract it by the cost of the user coffe choice
                profit += MENU[user_input]["cost"]
                print(f"Here is {round(Cost)} in change.")
                print(f"“Here is your {user_input}. Enjoy!”")
            else:
                print("Sorry that's not enough money. Money Refunded")
