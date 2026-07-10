###############################################################
# PROJECT 7: Object-Oriented Inventory System
#
# Goal:
# Replace dictionaries with Python classes.
#
# NEW CONCEPT:
# Object-Oriented Programming
#
# Create a class:
#
# InventoryItem
# Attributes
# ----------
# item
# category
# quantity
# price
#
# Methods
# -------
# inventory_value()

import json


class InventoryItem:
    def __init__(self, item, category, quantity, price):
        self.item = item
        self.category = category
        self.quantity = quantity
        self.price = price
    
    def inventory_value(self):
        return self.price * self.quantity
        

# Build another class:
#
# InventoryManager
#
# Responsibilities
# ----------------
# Load inventory
# Add products
# Remove products
# Calculate totals
# Find highest value item
# Generate report



class InventoryManager:
    def __init__(self):
        self.items = []

    def load_item(self,filename):
        with open(filename,'r',encoding='UTF-8') as file:
            data = json.load(file)
        for record in data:
            self.add_item(record)
        
    def add_item(self, record):
            try:
                self.items.append(InventoryItem(record['item'],record['category'],record['quantity'],record['price']))
            except KeyError:
                self.items.append(InventoryItem(record['item'],record['category'],record.get('quantity',0),record.get('price',0)))
            if record['quantity'] <= 0:
                self.items.remove(record)
            elif record['price'] <= 0:
                self.items.remove(record)
    
    def remove_item(self,record):
        self.items = [i for i in self.items if i.item != record]
    
    # Practice problem: Write a function add_to_cart(cart, item) where cart is a list. 
    # The function should add the item and return the updated cart. 
    # Verify that return cart.append(item) does not work, then fix it so it does.
    # def add_to_cart(cart:list,item):
    #     cart.append(item)
    # Just so I understand correctly, if I update an iterable inside of a function, do not use the return keyword?


    def calculate_totals(self):
        new_dict = {}
        for record in self.items:
            category = record.category
            total = record.inventory_value()
            if category not in new_dict:
                new_dict[category] = 0
            new_dict[category] += total
        return new_dict
    
    def total_inventory_value(self):
        total = 0
        try:
            for record in self.items:
                total += record['inventory_value']
        except ValueError:
            print('No Values')
        return total
    
    def highest_value_item(self):
        try:
            top_item = max(self.items,key=lambda x:x.inventory_value())
            top_tuple = (top_item.item,top_item.inventory_value())
        except ValueError:
            print('No Values in List')
        return top_tuple
    
    def generate_report(self, total_value, top_item, category_values, records):
        return f'''
    INVENTORY REPORT
    ----------------

    Total Inventory Value:
    ${total_value}

    Highest Value Item:
    {top_item}

    Category Totals:
    {category_values}

    Inventory Records:
    {records}
    '''


#
# Skills
# -------
# ✓ Classes
# ✓ Objects
# ✓ Constructors
# ✓ Methods
# ✓ Object collections
#
###############################################################