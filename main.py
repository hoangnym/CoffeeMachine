# Import libraries
import data


# use data import and assign value
menu = data.menu
resources = data.resources


# Defining functions
# Take order function
def take_order(name):
    """
    Accepts name and returns order.
    :param name: name
    :return: drink
    """
    order = input("What would you like? (espresso/latte/cappuccino): ").lower()

    # Check if order equals report
    while order == "report":
        order = print_report()

    if order in ("espresso", "latte", "cappuccino"):
        enough = check_resources(menu[order])
        if enough == "enough":
            drink = menu[order]
            make_coffee(drink)
        else:
            drink = check_resources(menu[order])
            print(drink)
    elif order == "off":
        drink = "off"

    return drink


# TODO: 1. Print report of all coffee machine resources
def print_report():
    for ingredient in resources:
        print(f"{ingredient}: {resources[ingredient][0]}{resources[ingredient][1]}")
    order = input("What would you like? (espresso/latte/cappuccino): ").lower()
    return order


# TODO: 2. Check resources sufficient to make drink order
def check_resources(drink):
    for ingredient in drink['ingredients']:
        if drink['ingredients'][ingredient] > resources[ingredient][0]:
            return f"Sorry there is not enough {ingredient}"
    return "enough"


# TODO: 3. Process coins


# TODO: 4. Check if transaction successful


# TODO: 5. Make coffee
def make_coffee(drink):
    for ingredient in drink['ingredients']:
        resources[ingredient][0] -= drink['ingredients'][ingredient]
    resources['money'][0] += drink['cost']
    print(resources)


# Run program
if __name__ == '__main__':
    # Ask new customer for name
    name = input("Welcome to Puzzles, what is your first name?: ").capitalize()
    print(f'Hi, {name}')

    taking_orders = True

    # Take order of new customer
    while taking_orders:
        order = take_order(name)
        if order == "off":
            taking_orders = False

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
