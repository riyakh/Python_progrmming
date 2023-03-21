
Money = 0
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk":0,
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


def generate_report(money):
    print(f"Water: {resources['water']}")
    print(f"Milk: {resources['milk']}")
    print(f"Coffee: {resources['coffee']}")
    print(f"Money: {money}")


def resource_check(coffee):
    if resources['water'] < MENU[coffee]['ingredients']['water']:
        print("Sorry there is not enough water")
        coffee_machine()
    elif resources['milk'] < MENU[coffee]['ingredients']['milk']:
        print("Sorry there is not enough milk")
        coffee_machine()
    elif resources['coffee'] < MENU[coffee]['ingredients']['coffee']:
        print("Sorry there is not enough coffee")
        coffee_machine()


def coin_calculation(quarter, dime, nickle, penny, coffee):
    total_money = .25 * quarter + .1 * dime + .05 * nickle + .01 * penny
    if total_money < MENU[coffee]['cost']:
        print("Sorry that's not enough Money. Money Refunded.")
        coffee_machine()
    else:
        due_amount = round(total_money - MENU[coffee]['cost'],2)
        resources['water'] -= MENU[coffee]['ingredients']['water']
        resources['milk'] -= MENU[coffee]['ingredients']['milk']
        resources['coffee'] -= MENU[coffee]['ingredients']['coffee']
        global profit
        profit += MENU[coffee]['cost']
        print(f"here is ${due_amount} in change")
        print(f"Here is your {coffee}. Enjoy")
        coffee_machine()


def coffee_machine():
    coffee_type = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if coffee_type == 'report':
        generate_report(profit)
        coffee_machine()
    elif coffee_type == 'espresso' or coffee_type == 'latte' or coffee_type == 'cappuccino':
        resource_check(coffee_type)
        print("Please insert the coin.")
        quarters = int(input("how many quarters?: "))
        dimes = int(input("how many dimes?: "))
        nickles = int(input("how many quarters?: "))
        pennies = int(input("how many pennies?: "))
        coin_calculation(quarters, dimes, nickles, pennies, coffee_type)


coffee_machine()