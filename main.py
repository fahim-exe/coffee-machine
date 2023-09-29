import coffee_machine as Coffee

#1- 3 hot flavors
#2- espresso, latte, cappuccino
#3- espresso: 50ml w, 18g coffee; latte: 200ml w, 24g coffee, 150ml milk; cupp: 250ml w, 24g coffee, 100ml milk
#4- tank: 300ml w, 200ml milk, 100g coffee
#5- report: checks available resources
#6- check resources are sufficient
#7- coin operated
#8- process coins and check for successful transaction
#9- successful transaction> check available resources
#10- if resources available make coffee and deduct resources
#11- espresso 1$, latte 2.50$, cuppuccino 3.5$
#12- quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01

tank = {'water': 300, 'milk':200, 'coffee':100, 'money':0}

while True:
    user_input = input("What would you like? \nEspresso: 1$ \nLatte: 2.50$ \nCuppuccino:3.5$ \nPlease select your coffee:").lower()

    if user_input=="off":
        exit()

    if user_input=="report":
        print(f"Water: {tank['water']}ml")
        print(f"Milk: {tank['milk']}ml")
        print(f"Coffee: {tank['coffee']}")
        print(f"Money: ${tank['money']}")
        print()
    
    if user_input=="latte":
        pass

    if user_input=="cuppuccino":
        pass

    if user_input=="espresso":
        pass

    if user_input=="reset":
        pass

    if user_input=="refill":
        pass
         