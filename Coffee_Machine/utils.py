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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}


#
# def report(left):
#     water_left = available_water - required_water
#     milk_left = available_milk - required_milk
#     coffee_left = available_coffee - required_coffee
#
#
# def format_data(recipe):
#     input("What would you like?(espresso/latte/cappuccino): ")
#     water = recipe["water"]
#     milk = recipe["milk"]
#     coffee = recipe["coffee"]
#     return f"Water : {water} ml\n" \
#            f"Milk : {milk} ml\n" \
#            f"Coffee : {coffee}g\n" \
#            f"Money : ${money}"
#
#
# def check_resources():
#     if available_water < required_water:
#         print("Sorry there is insufficient water")
#     elif available_milk < required_milk:
#         print("Sorry there is insufficient milk")
#     elif available_coffee < required_coffee:
#         print("Sorry there is insufficient coffee")
#

def format_report(recipe):
    water = recipe["water"]
    milk = recipe["milk"]
    coffee = recipe["coffee"]
    money = recipe["money"]

    return f"Water : {water} ml\n" \
           f"Milk : {milk} ml\n" \
           f"Coffee : {coffee}g\n" \
           f"Money : ${money}"


def coins():
    print("Please insert some coins.")
    quarters = int(input("How many quarters?: ")) * 0.25
    dimes = int(input("How many dimes?: ")) * 0.10
    nickles = int(input("How many nickles?: ")) * 0.05
    pennies = int(input("How many pennies?: ")) * 0.01
    amount = quarters + dimes + nickles + pennies
    return amount


def transaction_successful(cost, amount):
    if cost < amount:
        return True
    else:
        return False


def check_resources(ingredients, resources, coffee_pref):
    required_water = ingredients[coffee_pref]['ingredients']['water']
    required_milk = ingredients[coffee_pref]['ingredients']['milk']
    required_coffee = ingredients[coffee_pref]['ingredients']['coffee']

    available_water = resources['water']
    available_milk = resources['milk']
    available_coffee = resources['coffee']

    if required_water > available_water:
        print("Sorry there is not enough water")
        return False
    elif required_milk > available_milk:
        print("Sorry there is not enough milk")
        return False
    elif required_coffee > available_coffee:
        print("Sorry there is not enough coffee")
        return False
    else:
        resources["water"] = available_water - required_water
        resources["milk"] = available_milk - required_milk
        resources["coffee"] = available_coffee - required_coffee
        resources["money"] += ingredients[coffee_pref]['cost']

        return True
