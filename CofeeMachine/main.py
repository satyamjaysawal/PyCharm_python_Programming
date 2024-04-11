class CoffeeMachine:
    def __init__(self):
        self.water = 500
        self.milk = 500
        self.coffee_beans = 200
        self.cups = 10
        self.money = 0

    def display_menu(self):
        print("Welcome to the Coffee Machine!")
        print("Menu:")
        print("1. Espresso - Rs 30")
        print("2. Latte - Rs 35")
        print("3. Cappuccino - Rs 40")
        print("4. Exit")

    def process_order(self, choice):
        if choice == 1:  # Espresso
            if self.check_inventory(250, 0, 16):
                self.make_coffee(250, 0, 16, 30)
        elif choice == 2:  # Latte
            if self.check_inventory(200, 150, 20):
                self.make_coffee(200, 150, 20, 35)
        elif choice == 3:  # Cappuccino
            if self.check_inventory(250, 100, 20):
                self.make_coffee(250, 100, 20, 40)
        elif choice == 4:
            print("Exiting...")
            return
        else:
            print("Invalid choice. Please select a valid option.")

    def check_inventory(self, water_needed, milk_needed, beans_needed):
        if self.water < water_needed:
            print("Sorry, not enough water!")
            return False
        elif self.milk < milk_needed:
            print("Sorry, not enough milk!")
            return False
        elif self.coffee_beans < beans_needed:
            print("Sorry, not enough coffee beans!")
            return False
        elif self.cups == 0:
            print("Sorry, not enough cups!")
            return False
        else:
            return True

    def make_coffee(self, water_needed, milk_needed, beans_needed, cost):
        print("Making coffee...")
        self.water -= water_needed
        self.milk -= milk_needed
        self.coffee_beans -= beans_needed
        self.cups -= 1
        self.money += cost
        print("Here is your coffee! Enjoy!")

    def report(self):
        print(f"Water: {self.water}ml")
        print(f"Milk: {self.milk}ml")
        print(f"Coffee Beans: {self.coffee_beans}g")
        print(f"Cups: {self.cups}")
        print(f"Money: Rs {self.money}")

# Main program loop
if __name__ == "__main__":
    coffee_machine = CoffeeMachine()

    while True:
        coffee_machine.display_menu()
        choice = int(input("Please select an option: "))
        coffee_machine.process_order(choice)
        if choice == 4:
            break

    coffee_machine.report()
