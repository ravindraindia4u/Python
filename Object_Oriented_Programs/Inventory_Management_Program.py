"""
Extend the above program to Create InventoryManager to manage the
Inventory. The Inventory Manager will use InventoryFactory to create Inventory
Object from JSON. The InventoryManager will call each Inventory Object in its list
to calculate the Inventory Price and then call the Inventory Object to return the
JSON String. The main program will be with InventoryManager
"""

import json

from Object_Oriented_Programs.Inventory_data import main


class Inventory:
    def __init__(self, dictionary):
        self.name = dictionary.get("Name")
        self.weight = dictionary.get("Weight")
        self.price = dictionary.get("Price per kg")


class InventoryManager:
    def __init__(self):
        self.list = []

    def calculate_price(self):
        Sum = 0
        for obj in self.list:
            Sum += obj.price * obj.weight
        return Sum


obj_inventory_manager = InventoryManager()

file = open("inventory", 'r')
data = json.load(file)
file.close()

for key, value in data.items():
    for dictionary in value:
        obj = Inventory(dictionary)
        obj_inventory_manager.list.append(obj)

print(f"The total inventory price of our stock is : {obj_inventory_manager.calculate_price()} rs/-")