from file_handler import load_inventory, save_report
from validation import clean_inventory
from inventory import build_inventory_records, category_totals, highest_value_item, total_inventory_value
from reporting import generate_report


inventory = load_inventory('inventory_app(projects 6-10)/assets/messy_inventory.json')
cleaned_inventory = clean_inventory(inventory)
inventory_records = build_inventory_records(cleaned_inventory)



report = save_report(
                    generate_report(inventory_records, 
                    category_totals(inventory_records), 
                    highest_value_item(inventory_records), 
                    total_inventory_value(inventory_records)),
                    'assets/project6_inventory_report.txt')



