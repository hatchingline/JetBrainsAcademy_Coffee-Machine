class CoffeeMachine:
    def __init__(self, water, milk, beans, cups, money, ):
        self.water = water
        self.milk = milk
        self.beans = beans
        self.cups = cups
        self.money = money
        self.user_input = None
        self.coffee_option = None
        self.machine_run = True

    def remaining(self):
        print("The coffee machine has:\n{} of water\n{} of milk\n{} of coffee beans\n{} of disposable cups\n${} of money".format(self.water, self.milk, self.beans, self.cups, self.money))

    def espresso(self):
        if self.water >= 250 and self.beans >= 16 and self.cups >= 1:
            print("I have enough resources, making you a coffee!")
            self.water -= 250
            self.beans -= 16
            self.cups -= 1
            self.money += 4
        elif self.water < 250:
            print("Sorry, not enough water!")
        elif self.beans < 16:
            print("Sorry, not enough coffee beans!")
        elif self.cups < 1:
            print("Sorry, not enough disposable cups!")

    def latte(self):
        if self.water >= 350 and self.milk >= 75 and self.beans >= 20 and self.cups >= 1:
            print("I have enough resources, making you a coffee!")
            self.water -= 350
            self.milk -= 75
            self.beans -= 20
            self.cups -= 1
            self.money += 7
        elif self.water < 350:
            print("Sorry, not enough water!")
        elif self.milk < 75:
            print("Sorry, not enough milk!")
        elif self.beans < 20:
            print("Sorry, not enough coffee beans!")
        elif self.cups < 1:
            print("Sorry, not enough disposable cups!")

    def cappuccino(self):
        if self.water >= 200 and self.milk >= 100 and self.beans >= 12 and self.cups >= 1:
            print("I have enough resources, making you a coffee!")
            self.water -= 200
            self.milk -= 100
            self.beans -= 12
            self.cups -= 1
            self.money += 6
        elif self.water < 200:
            print("Sorry, not enough water!")
        elif self.milk < 100:
            print("Sorry, not enough milk!")
        elif self.beans < 12:
            print("Sorry, not enough coffee beans!")
        elif self.cups < 1:
            print("Sorry, not enough disposable cups!")

    def buy(self):
        self.coffee_option = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        if self.coffee_option == "1":
            self.espresso()
        elif self.coffee_option == "2":
            self.latte()
        elif self.coffee_option == "3":
            self.cappuccino()
        elif self.coffee_option == "back":
            pass

    def fill(self):
        self.water += int(input("Write how many ml of water do you want to add:"))
        self.milk += int(input("Write how many ml of milk do you want to add:"))
        self.beans += int(input("Write how many grams of coffee beans do you want to add:"))
        self.cups += int(input("Write how many disposable cups of coffee do you want to add:"))

    def take(self):
        print("I gave you ${}".format(self.money))
        self.money = 0

    def take_user_input(self):
        self.user_input = input("Write action (buy, fill, take, remaining, exit):")
        if self.user_input == "remaining":
            self.remaining()
        elif self.user_input == "buy":
            self.buy()
        elif self.user_input == "fill":
            self.fill()
        elif self.user_input == "take":
            self.take()
        elif self.user_input == "exit":
            self.machine_run = False


coffee_machine = CoffeeMachine(400, 540, 120, 9, 550)
while coffee_machine.machine_run:
    coffee_machine.take_user_input()
