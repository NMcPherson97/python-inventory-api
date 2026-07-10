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