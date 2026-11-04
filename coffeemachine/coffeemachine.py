class CoffeeMachine:
    def __init__(self):
        self.water = 400
        self.milk = 540
        self.beans = 120
        self.cups = 9
        self.money = 550
        self.state = "CHOOSING_ACTION"
        self.start()

    def start(self):
        print("\nWrite action (buy, fill, take, remaining, exit):")

    def process_input(self, user_input):
        if self.state == "CHOOSING_ACTION":
            if user_input == "buy":
                self.state = "CHOOSING_COFFEE"
                print("\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
            elif user_input == "fill":
                self.state = "FILLING_WATER"
                print("\nWrite how many ml of water you want to add:")
            elif user_input == "take":
                self.take()
                self.start()
            elif user_input == "remaining":
                self.remaining()
                self.start()
            elif user_input == "exit":
                return False

        elif self.state == "CHOOSING_COFFEE":
            self.buy(user_input)
            self.state = "CHOOSING_ACTION"
            self.start()

        elif self.state == "FILLING_WATER":
            self.water += int(user_input)
            self.state = "FILLING_MILK"
            print("Write how many ml of milk you want to add:")

        elif self.state == "FILLING_MILK":
            self.milk += int(user_input)
            self.state = "FILLING_BEANS"
            print("Write how many grams of coffee beans you want to add:")

        elif self.state == "FILLING_BEANS":
            self.beans += int(user_input)
            self.state = "FILLING_CUPS"
            print("Write how many disposable coffee cups you want to add:")

        elif self.state == "FILLING_CUPS":
            self.cups += int(user_input)
            self.state = "CHOOSING_ACTION"
            self.start()

        return True

    def check_resources(self, req_water, req_milk, req_beans):
        if self.water < req_water:
            print("Sorry, not enough water!")
            return False
        if self.milk < req_milk:
            print("Sorry, not enough milk!")
            return False
        if self.beans < req_beans:
            print("Sorry, not enough coffee beans!")
            return False
        if self.cups < 1:
            print("Sorry, not enough disposable cups!")
            return False
        print("I have enough resources, making you a coffee!")
        return True

    def buy(self, choice):
        if choice == '1':
            if self.check_resources(250, 0, 16):
                self.water -= 250
                self.beans -= 16
                self.cups -= 1
                self.money += 4
        elif choice == '2':
            if self.check_resources(350, 75, 20):
                self.water -= 350
                self.milk -= 75
                self.beans -= 20
                self.cups -= 1
                self.money += 7
        elif choice == '3':
            if self.check_resources(200, 100, 12):
                self.water -= 200
                self.milk -= 100
                self.beans -= 12
                self.cups -= 1
                self.money += 6
        elif choice == 'back':
            pass

    def take(self):
        print(f"\nI gave you {self.money}")
        self.money = 0

    def remaining(self):
        print("\nThe coffee machine has:")
        print(f"{self.water} of water")
        print(f"{self.milk} of milk")
        print(f"{self.beans} of coffee beans")
        print(f"{self.cups} of disposable cups")
        print(f"{self.money} of money")


machine = CoffeeMachine()
running = True

while running:
    user_input = input()
    running = machine.process_input(user_input)

