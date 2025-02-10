from typing import Dict,Optional
from computer import Computer
class ResaleShop:
    # What attributes will it need?
    inventory:list
    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self,inventory:list):
        self.inventory=inventory
         # You'll remove this when you fill out your constructor
    # What methods will you need?
    # buy a computer (adds computer to inventory)
    def buy(self,computer:Computer):
        self.inventory.append(computer)
        return self.inventory.index(computer)
    # sell a computer (deletes computer from inventory)
    def sell(self,item_id:int):
        if 0<=item_id<len(self.inventory):
            self.inventory.pop(item_id)
        else:
            print("Item", item_id, "not found. Please select another item to sell.")
    # update price (call from resaleshop class, not from computer class)
    def update_price(self,item_id:int,new_price:int):
        if 0<=item_id<len(self.inventory):
            self.inventory[item_id].upd_price(new_price)
        else:
            print("Item", item_id, "not found. Cannot update price.")
    # refurbish the computer
    def refurbish(self,item_id:int,new_os:Optional[str]=None):
        if 0<=item_id<len(self.inventory):
            computer=self.inventory[item_id]
            if computer.year_made<2000:
                computer.upd_price(0)
            elif computer.year_made<2012:
                computer.upd_price(250)
            elif computer.year_made<2018:
                computer.upd_price(550)
            else:
                computer.upd_price(1000)
            if new_os is not None:
                computer.upd_os(new_os)
        else:
            print("Item", item_id, "not found. Please select another item to refurbish.")
    # print out the objects in the inventory
    def print_inventory(self):
        if self.inventory:
            for item in self.inventory:
                print(f'Item ID: {self.inventory.index(item)} : {item}')
        else:
            print("No inventory to display.")

def main():
    shop=ResaleShop([])

    # First, let's make a computer
    computer = Computer(
        "Mac Pro (Late 2013)",
        "3.5 GHc 6-Core Intel Xeon E5",
        1024, 64,
        "macOS Big Sur", 2013, 1500
    )

    # Print a little banner
    print("-" * 21)
    print("COMPUTER RESALE STORE")
    print("-" * 21)

    # Add it to the resale store's inventory
    print("Buying", computer.description)
    print("Adding to inventory...")
    computer_id = shop.buy(computer)
    print("Done.\n")

    # Make sure it worked by checking inventory
    print("Checking inventory...")
    shop.print_inventory()
    print("Done.\n")
    
    # Manually updates price
    print("Updating price...")
    shop.update_price(computer_id,300)
    print(f"The new price is:{shop.inventory[computer_id].price}")
    print("Done.\n")
    
    # Now, let's refurbish it
    new_OS = "MacOS Monterey"
    print("Refurbishing Item ID:", computer_id, ", updating OS to", new_OS)
    print("Updating inventory...")
    shop.refurbish(computer_id, new_OS)
    print("Done.\n")

    # Make sure it worked by checking inventory
    print("Checking inventory...")
    shop.print_inventory()
    print("Done.\n")
    
    # Now, let's sell it!
    print("Selling Item ID:", computer_id)
    shop.sell(computer_id)
    
    # Make sure it worked by checking inventory
    print("Checking inventory...")
    shop.print_inventory()
    print("Done.\n")


# Calls the main() function when this file is run
if __name__ == "__main__": main()
