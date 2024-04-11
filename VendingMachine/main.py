class VendingMachine:
    def __init__(self):
        self.items = {"cola": 15, "chips": 10, "candy": 5}
        self.coins = {"10 rupees": 10, "5 rupees": 5, "2 rupees": 2, "1 rupee": 1}
        self.balance = 0

    def display_menu(self):
        print("Welcome to the Vending Machine!")
        print("Items available:")
        for item, price in self.items.items():
            print(f"- {item.capitalize()}: ₹{price}")
        print("\nCoins accepted: 10 rupees, 5 rupees, 2 rupees, 1 rupee")
        print("To select an item, enter its name. To exit, type 'exit'.")

    def insert_coins(self):
        print("\nAccepted Coins: 10 rupees, 5 rupees, 2 rupees, 1 rupee")
        while True:
            coin = input("Insert coin (type 'done' when finished): ").lower()
            if coin == 'done':
                break
            elif coin in self.coins:
                self.balance += self.coins[coin]
            else:
                print("Invalid coin. Please insert a valid coin.")

    def select_item(self, item):
        if item in self.items:
            price = self.items[item]
            if self.balance >= price:
                print(f"Here is your {item}! Enjoy!")
                self.balance -= price
            else:
                print("Insufficient funds. Please insert more coins.")
        else:
            print("Invalid item. Please select a valid item.")

    def return_change(self):
        if self.balance > 0:
            print(f"Returning change: ₹{self.balance}")
            self.balance = 0

# Main program loop
if __name__ == "__main__":
    vending_machine = VendingMachine()

    while True:
        vending_machine.display_menu()
        selection = input("\nSelect item: ").lower()
        
        if selection == 'exit':
            vending_machine.return_change()
            print("Exiting...")
            break
        else:
            vending_machine.insert_coins()
            vending_machine.select_item(selection)
