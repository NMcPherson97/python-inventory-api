import json

def load_inventory(filename):
        try:
            with open(filename) as file:
                data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            data = []
        return data
inventory = load_inventory('inventory_app(projects 6-10)/assets/messy_inventory.json')

def save_report(report, filename):
    with open(filename,'w',encoding='UTF-8') as file:
        file.write(report)
        
