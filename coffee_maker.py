logo = '''

  /$$$$$$             /$$$$$$   /$$$$$$                            /$$      /$$           /$$                          
 /$$__  $$           /$$__  $$ /$$__  $$                          | $$$    /$$$          | $$                          
| $$  \__/  /$$$$$$ | $$  \__/| $$  \__/  /$$$$$$   /$$$$$$       | $$$$  /$$$$  /$$$$$$ | $$   /$$  /$$$$$$   /$$$$$$ 
| $$       /$$__  $$| $$$$    | $$$$     /$$__  $$ /$$__  $$      | $$ $$/$$ $$ |____  $$| $$  /$$/ /$$__  $$ /$$__  $$
| $$      | $$  \ $$| $$_/    | $$_/    | $$$$$$$$| $$$$$$$$      | $$  $$$| $$  /$$$$$$$| $$$$$$/ | $$$$$$$$| $$  \__/
| $$    $$| $$  | $$| $$      | $$      | $$_____/| $$_____/      | $$\  $ | $$ /$$__  $$| $$_  $$ | $$_____/| $$      
|  $$$$$$/|  $$$$$$/| $$      | $$      |  $$$$$$$|  $$$$$$$      | $$ \/  | $$|  $$$$$$$| $$ \  $$|  $$$$$$$| $$      
 \______/  \______/ |__/      |__/       \_______/ \_______/      |__/     |__/ \_______/|__/  \__/ \_______/|__/      
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
'''

print(logo)

resources = {
    "water": 1000,
    "coffee": 300,
    "milk": 750,
    "money": float(0)
}

pricing = {
    "espresso": 1.5,
    "latte": 2,
    "cappuccino": 3
}

ingredients = {
    "espresso": {"water": 50, "milk": 0, "coffee": 18, "money": 1.5},
    "latte": {"water": 200, "milk": 150, "coffee": 24, "money": 2},
    "cappuccino": {"water": 250, "milk": 100, "coffee": 24, "money": 3}
}

continue_running = True


def money(quarters, dimes, nickels, pennies):
    total = int(quarters) * 0.25
    total += int(dimes) * 0.1
    total += int(nickels) * 0.05
    total += int(pennies) * 0.01
    return total


def handle_resources(coffee):
    for item in ingredients:
        if coffee == item:
            resources["water"] -= ingredients[item]["water"]
            resources["milk"] -= ingredients[item]["milk"]
            resources["coffee"] -= ingredients[item]["coffee"]
            resources["money"] += ingredients[item]["money"]

while continue_running:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if choice == "report":
        print(resources)
    else:
        print("\nPlease insert coins.\n")
        quarters = input("Quarters : ")
        dimes = input("Dimes : ")
        nickels = input("Nickels : ")
        pennies = input("Pennies : ")
        total_money = money(quarters, dimes, nickels, pennies)
        total_money -= pricing[choice]
        handle_resources(choice)
        print(f"Here is your ${total_money} in change.")
        print(f"Enjoy your {choice}!")
    print("\n\n")