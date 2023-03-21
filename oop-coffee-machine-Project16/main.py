from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_on = 'True'
menu = Menu()
money_machine = MoneyMachine()
coffeemaker = CoffeeMaker()

while is_on:
    choice = input(f"What would you like? ({menu.get_items()}):").lower()
    if choice == 'off':
        is_on = 'False'
    elif choice == 'report':
        coffeemaker.report()
        money_machine.report()
    else:
        option = menu.find_drink(choice)
        received_money = money_machine.money_received()
