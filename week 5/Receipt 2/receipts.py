import csv
from datetime import datetime

PRICE_INDEX = 2
NAME_INDEX = 1
PRODUCT_INDEX = 0
TAX_RATE = 0.06

def read_dictionary(filename, key_column_index=PRODUCT_INDEX):
    """Read the content of a CSV file into a compound dictionary and return the dictionary.
    Parameters:
        filename: the name of the CSV file to read.
        key_column_index: the index of the column to use as the keys in the dictionary.
    Return: a compound dictionary that contains the contents of the CSV file.
    """
    products_dict = {}
    try:
        with open(filename, 'rt') as csv_file:
            reader = csv.reader(csv_file)
            next(reader) 
            for row in reader:
                key = row[key_column_index]
                name = row[NAME_INDEX]
                price = float(row[PRICE_INDEX])
                products_dict[key] = [key, name, price]
    except FileNotFoundError as not_found_err:
        print(not_found_err)
    except PermissionError as perm_err:
        print(perm_err)
    return products_dict

def calculate_totals(products_dict, request_filename):
    ordered_items = []
    subtotal = 0.0
    total_items = 0

    try:
        with open(request_filename, 'rt') as request_file:
            request_reader = csv.reader(request_file)
            next(request_reader) 
            
            for row in request_reader:
                product_number = row[PRODUCT_INDEX]
                requested_quantity = int(row[1])
                
                try:
                    product_info = products_dict[product_number]
                    product_name = product_info[1]
                    product_price = product_info[2]
                    
                    item_total = requested_quantity * product_price
                    subtotal += item_total
                    total_items += requested_quantity
                    
                    ordered_items.append({
                        'name': product_name,
                        'quantity': requested_quantity,
                        'price': product_price,
                        'item_total': item_total
                    })
                
                except KeyError as key_err:
                    print(type(key_err).__name__, key_err)
                
    except FileNotFoundError as not_found_err:
        print(not_found_err)
    except PermissionError as perm_err:
        print(perm_err)

    return ordered_items, subtotal, total_items

def calculate_tax(subtotal):
    return subtotal * TAX_RATE

def print_receipt(store_name, ordered_items, total_items, subtotal, tax_amount, total_amount, timestamp):
    print(f"{store_name}\n")
    for item in ordered_items:
        print(f"{item['name']}: {item['quantity']} @ ${item['price']:.2f}")
    print(f"Number of Items: {total_items}")
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Sales Tax: ${tax_amount:.2f}")
    print(f"Total: ${total_amount:.2f}")
    print("\nThank you for shopping at the Inkom Emporium.")
    print(f"{timestamp.strftime('%a %b %d %H:%M:%S %Y')}")

def main():
    store_name = "Inkom Emporium"
    products_dict = read_dictionary("products.csv")
    
    if products_dict:
        ordered_items, subtotal, total_items = calculate_totals(products_dict, "request.csv")
        tax_amount = calculate_tax(subtotal)
        total_amount = subtotal + tax_amount
        timestamp = datetime.now() 
        
        print_receipt(store_name, ordered_items, total_items, subtotal, tax_amount, total_amount, timestamp)
    
if __name__ == "__main__":
    main()
