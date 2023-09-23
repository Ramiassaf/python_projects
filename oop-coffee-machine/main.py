# Import necessary classes from separate modules
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Create objects of the imported classes
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

# Set the initial state of the coffee machine to "on"
is_on = True

# Start an infinite loop to allow the user to order drinks
while is_on:

    # Prompt the user to choose a drink from the menu
    choice = input(f"What do you want to drink {menu.get_items()}? ")

    # If the user enters "off", turn off the coffee machine
    if choice == "off":
        print("Maintenance Mode")
        is_on = False

    # If the user enters "report", print a report of the coffee machine's resources and money
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()

    # If the user enters a drink name, check if the coffee machine has enough resources and the user has enough money
    elif choice in menu.get_items():  # Check if the item is in the menu
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            # If the user enters a drink name, check if the coffee machine has enough resources
            # And the user has enough money
            # If there are enough resources and the user has paid, make the drink
            coffee_maker.make_coffee(drink)

    else:
        menu.find_drink(choice)  # it Will print Sorry that item is not available.
