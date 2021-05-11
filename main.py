# Import libraries
import data


# use data import
menu = data.menu
resources = data.resources


# Defining functions
# Take order function
def take_order(name):
    '''
    Accepts name and returns order
    :param name: name
    :return: order
    '''
    print(f'Hi, {name}')
    order = input("What would you like? (espresso/latte/cappuccino): ").lower()



    return order

# TODO: 1. Print report of all coffee machine resources
def print_report():
    for key in resources:
        print(f"{key}: {resources[key]}")


# TODO: 2. Check resources sufficient to make drink order


# TODO: 3. Process coins


# TODO: 4. Check if transaction successful



# TODO: 5. Make coffee



# Run program
if __name__ == '__main__':
    # Ask new customer for name
    name = input("Welcome to Puzzles, what is your first name?: ").capitalize()

    if name == "report":
        print_report()

    # Take order of new customer
    order = take_order(name)
    print(order)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
