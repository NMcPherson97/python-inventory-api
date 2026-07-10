###############################################################
# PROJECT 8: SQLite Inventory Database
#
# Goal:
# Replace JSON storage with a relational database.
#
# NEW CONCEPT:
# SQLite
#
# Create:
#
# inventory.db
#
# Table
# -----
#
# inventory
#
# Columns
# --------
# id
# item
# category
# quantity
# price
#
# Functions
# ----------
#

import json
import sqlite3
# Create database
def create_database():
    conn = sqlite3.connect('inventory_app(projects 6-10)/assets/inventory.db')
    return conn

my_db = create_database()

#Load inventory
def load_inventory(filename):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
    except(FileNotFoundError, json.JSONDecodeError):
            data = []
    return data
inventory = load_inventory('inventory_app(projects 6-10)/assets/messy_inventory.json')

# Add items from inventory to database
def add_item(db):
    cursor = db.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS inventory(
                id integer PRIMARY KEY AUTOINCREMENT,
                item text UNIQUE,
                category text,
                quantity integer,
                price real,
                inventory_value real)
                """)
    for i in inventory:
        if isinstance(i.get('quantity'),(int,float)):
            cursor.execute("""INSERT OR IGNORE INTO inventory (item, category, quantity, price) VALUES (? ,?, ?, ?)""",
                          (i.get('item'),
                           i.get('category'),
                           i.get('quantity'),
                           i.get('price')))
    db.commit()

add_item(my_db)
    


# Remove items with negative or missing values
def remove_item(db):
    cursor = db.cursor()
    cursor.execute("""
        DELETE FROM inventory 
        WHERE price < 0 
           OR quantity < 0 
           OR price IS NULL 
           OR quantity IS NULL
    """)
    db.commit()

remove_item(my_db)


# Update the insert value column
def update_items(db):
    cursor = db.cursor()
    cursor.execute('UPDATE inventory SET inventory_value = price * quantity')
    db.commit()
update_items(my_db)

# build_inventory_records()
def build_inventory_records(db):
    cursor = db.cursor()
    cursor.execute('SELECT * FROM inventory')
    records = cursor.fetchall()
    db.commit()
    return records
    
build_inventory_records(my_db)
    

# category_totals()
def category_totals(db):
    cursor = db.cursor()
    cursor.execute("""SELECT SUM(inventory_value) 
                   FROM inventory
                   GROUP BY category """)
    result = cursor.fetchall()
    db.commit()
    return result
    
category_totals(my_db)


# highest_value_item()
def highest_value_item(db):
    cursor = db.cursor()
    cursor.execute("""SELECT *
                   FROM inventory
                   ORDER BY inventory_value DESC LIMIT 1 """)
    highest_value = cursor.fetchall()
    db.commit()
    return highest_value
    
highest_value_item(my_db)

# total_inventory_value()
def total_inventory_value(db):
    cursor = db.cursor()
    cursor.execute("""SELECT SUM(inventory_value) FROM inventory""")
    total_inventory = cursor.fetchall()
    db.commit()
    return total_inventory
    

total_inventory_value(my_db)

# generate_report()
def generate_report(records, category_values, total_value, top_item):
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

print(generate_report(build_inventory_records(my_db),category_totals(my_db),total_inventory_value(my_db),highest_value_item(my_db)))

# Skills
# -------
# ✓ sqlite3
# ✓ SQL CRUD
# ✓ Database schema
# ✓ Connecting Python to SQL
#
###############################################################