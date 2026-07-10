def build_inventory_records(clean_inventory):
    new_list = []
    for item in clean_inventory:
        new_dict = item.copy()
        new_dict['inventory_value'] = item['quantity'] * item['price']
        new_list.append(new_dict)
    return new_list
# inventory_records = build_inventory_records(inventory_records)

def category_totals(records):
    new_dict = {}
    for record in records:
        category = record['category']
        total = record['inventory_value']
        if category not in new_dict:
            new_dict[category] = 0
        new_dict[category] += total
    return new_dict

def highest_value_item(records):
    try:
        top_item = max(records, key=lambda x: x['inventory_value'])
        top_tuple = (top_item['item'],top_item['inventory_value'])
    except ValueError:
        print('"Error: The inventory list is empty."')
    return top_tuple
    
def total_inventory_value(records):
    total = 0
    for record in records:
        total += record['inventory_value']  
    return total