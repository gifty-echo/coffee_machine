from utils import *

money = 0
Is_success = True
while Is_success:
    coffee_pref = input("What would you like?(espresso/latte/cappuccino): ")
    if coffee_pref == "report":
        print(format_report(resources))

    elif coffee_pref == "espresso":
        if check_resources(MENU, resources, coffee_pref):
            amount = coins()
            cost = MENU[coffee_pref]["cost"]
            if transaction_successful(cost=cost, amount=amount):
                change = amount - cost
                print(f"Here is ${round(change, 2)} in change")
                print(f"Here is your {coffee_pref}. Enjoy!")
            else:
                print("Sorry, money is insufficient. Money refunded.")

    elif coffee_pref == "latte":
        if check_resources(MENU, resources, coffee_pref):
            amount = coins()
            cost = MENU[coffee_pref]["cost"]
            if transaction_successful(cost=cost, amount=amount):
                change = amount - cost
                print(f"Here is ${round(change, 2)} in change")
                print(f"Here is your {coffee_pref}. Enjoy!")
            else:
                print("Sorry, money is insufficient. Money refunded.")

    elif coffee_pref == "cappuccino":
        if check_resources(MENU, resources, coffee_pref):
            amount = coins()
            cost = MENU[coffee_pref]["cost"]
            if transaction_successful(cost=cost, amount=amount):
                change = amount - cost
                print(f"Here is ${round(change, 2)} in change")
                print(f"Here is your {coffee_pref}. Enjoy!")
            else:
                print("Sorry, money is insufficient. Money refunded.")
