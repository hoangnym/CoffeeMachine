# Import libraries
import data


# use data import
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

    print(f'Hi, {name}')
    order = input("What would you like? (espresso/latte/cappuccino): ").lower()

    # Check if order equals report
    while order == "report":
        order = print_report()

    if order in ("espresso", "latte", "cappuccino"):
        if check_resources(menu[order]):
            drink = menu[order]

    return drink


# TODO: 1. Print report of all coffee machine resources
def print_report():
    for ingredient in resources:
        print(f"{ingredient}: {resources[ingredient][0], resources[ingredient][1]}")
    order = input("What would you like? (espresso/latte/cappuccino): ").lower()
    return order


# TODO: 2. Check resources sufficient to make drink order
def check_resources(drink):
    for ingredient in drink['ingredients']:
        if drink['ingredients'][ingredient] < resources[ingredient][0]:
            return f"Sorry there is not enough {ingredient}"
    return True


# TODO: 3. Process coins


# TODO: 4. Check if transaction successful



# TODO: 5. Make coffee
def make_coffee(drink):
    for ingredient in drink['ingredients']:
        resources[ingredient][0] = resources[ingredient][0] - drink['ingredients'][ingredient]



# Run program
if __name__ == '__main__':
    # Ask new customer for name
    name = input("Welcome to Puzzles, what is your first name?: ").capitalize()

    # Take order of new customer
    order = take_order(name)
    print(order)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
