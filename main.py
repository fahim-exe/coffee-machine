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
#11- espresso 0.5$, latte 1.50$, cuppuccino 2.5$
#12- quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01

tank = {'water': 300, 'milk':200, 'coffee':100, 'money':0}
internal = ["report", "off", "reset", "refill"]
menu = ["latte", "cappuccino", "espresso"]

while True:
    user_input = input("What would you like? \nEspresso: 0.50$ \nLatte: 1.50$ \nCuppuccino:2.5$ \nPlease select your coffee:").lower()
    print()

    if user_input in internal:

        if user_input=="off":
            exit()
            break

        if user_input=="report":
            print(f"Water: {tank['water']}ml")
            print(f"Milk: {tank['milk']}ml")
            print(f"Coffee: {tank['coffee']}g")
            print(f"Money: ${tank['money']}")
            print()

        if user_input=="reset":
            tank = {'water': 300, 'milk':200, 'coffee':100, 'money':0}
            print()
            continue

        if user_input=="refill":
            
            chk = input("Refill item (r) or Full refill (f): ").lower()
            if chk=="r":
                fill_item = input("Select one Coffee(c), Water(w), Milk(m): ")
                fill = int(input("Enter amount: "))
                if fill_item=="w":
                    tank['water'] = fill
                if fill_item=="m":
                    tank['milk'] = fill
                if fill_item=="c":
                    tank['coffee'] = fill         

                


            else:

                while True:
                    

                    w = int(input("Please enter water quantity: "))
                    m = int(input("Please enter milk quantity: "))
                    c = int(input("Please enter coffee quantity: "))

                    if w>300:
                        print("Please lessen water!!!")
                        continue

                    if m>200:
                        print("Please lessen milk!!!")
                        continue

                    if c>100:
                        print("Please lessen coffee!!!")
                        continue

                    if w>0 and w<301:
                        tank["water"] = w
                    if m>0 and m<201:
                        tank["milk"] = m
                    if c>0 and c<101:
                        tank["coffee"] = c
                    
                    print()
                    break

    if user_input in menu:
        q = int(input("How many quarters?: ")) #0.25
        d = int(input("How many dimes?: ")) #0.10
        n = int(input("How many nickels?: ")) #0.05
        p = int(input("How many pennies?: ")) #0.01

        paid = round((q*0.25)+(d*0.10)+(n*0.05)+(p*0.01), 2)
        check = Coffee.check_resources(tank, user_input)
        if check!=True:
                print("Machine Needs Servicing!!!!!")
                print(f"Please take the returned money ${paid}")
                print()
                continue
        


        if user_input=="espresso":
            if paid<0.5:
                print(f"Please take returned money ${paid}")
                print()
                continue

            change = round((paid-0.50), 2)
            
            

            if check:
                tank["money"] = tank['money']+0.50
                tank['water'] = tank["water"]-50
                tank["coffee"] = tank["coffee"]-18

                if change>0:
                    print(f"Here is ${change} in change.")               

                print("Here is your Espresso.... Enjoy!!!")
                print("")

        if user_input=="latte":
            if paid<1.5:
                print(f"Please take returned money ${paid}")
                print()
                continue
            change = paid-1.5
            
            if check:
                tank["money"] = tank['money']+1.5
                tank['water'] = tank["water"]-200
                tank["coffee"] = tank["coffee"]-24
                tank["milk"] = tank["milk"]-150

                if change>0:
                    print(f"Here is ${change} in change.")

                print("Here is your Latte.... Enjoy!!!")
                print("")

            

        if user_input=="cappuccino":
            if paid<2.5:
                print(f"Please take returned money ${paid}")
                print()
                continue
            change = paid-2.5
            
            if check:
                tank["money"] = tank['money']+2.5
                tank['water'] = tank["water"]-250
                tank["coffee"] = tank["coffee"]-24
                tank["milk"] = tank["milk"]-100

                if change>0:
                    print(f"Here is ${change} in change.")

                print("Here is your Cappuccino.... Enjoy!!!")
                print("")

            




    if user_input not in (internal+menu):
        print("Please enter a valid input!!!")
        print()

         