# from models import Item, ItemResponse, ItemUpdate
import sqlite3
import logging

logger = logging.getLogger(__name__)

def get_all_items(db):
    cursor = db.cursor()
    cursor.execute("SELECT * FROM inventory")
    return cursor.fetchall()

def get_item_by_id(db, item_id):
    logger.info("Fetching item id=%s", item_id)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM inventory WHERE id = ?", (item_id,))
    result = cursor.fetchone()
    if result is None:
        logger.warning("Item not found id=%s", item_id)
    return result

def create_item(db, item):
    cursor = db.cursor()
    cursor.execute(
        "INSERT INTO inventory (category, quantity, price) VALUES (?, ?, ?)",
        (item.category, item.quantity, item.price)
    )
    db.commit()
    new_id = cursor.lastrowid
    return get_item_by_id(db, new_id)

def update_item(db, item_id):
    cursor = db.cursor()
    cursor.execute("UPDATE inventory SET inventory_value = price * quantity")
    db.commit()
    return get_item_by_id(db, item_id)

def delete_item(db, item_id):
    cursor = db.cursor()
    cursor.execute("DELETE FROM inventory WHERE id = ?", (item_id,))
    db.commit()
    return cursor.rowcount > 0   # rowcount = number of rows affected

def get_category_totals(db):
    cursor = db.cursor()
    cursor.execute("SELECT category, SUM(inventory_value) FROM inventory GROUP BY category")
    return cursor.fetchall()

def get_highest_value_item(db):
    cursor = db.cursor()
    cursor.execute("SELECT * FROM inventory ORDER BY inventory_value DESC LIMIT 1")
    return cursor.fetchone()

def get_total_inventory_value(db):
    cursor = db.cursor()
    cursor.execute("SELECT SUM(inventory_value) FROM inventory")
    return cursor.fetchone()