def validate_inventory_item(item):
    required_keys = ['item','category','quantity','price']
    if not all(key in item for key in required_keys):
        return False
    # Check quantity
    if not isinstance(item["quantity"], (int, float)):
        return False
    if item["quantity"] < 0:
        return False

    # Check price
    if not isinstance(item["price"], (int, float)):
        return False
    if item["price"] < 0:
        return False

    return True

def clean_inventory(inventory):
    clean_list = []
    for item in inventory:
        if validate_inventory_item(item):
            clean_list.append(item)
    return clean_list

