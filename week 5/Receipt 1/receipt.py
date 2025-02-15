import csv

PRICE_INDEX = 2
NAME_INDEX = 1
PRODUCT_INDEX = 0

def read_dictionary(filename, key_column_index=PRODUCT_INDEX):
    """Read the content of a CSV file into a compound dictionary and return the dictionary.
    Parameters:
        filename: the name of the CSV file to read.
        key_column_index: the index of the column to use as the keys in the dictionary.
    Return: a compound dictionary that contains the contents of the CSV file.
    """
    products_dict = {}
    with open(filename, 'rt') as csv_file:
        reader = csv.reader(csv_file)
        next(reader)  
        for row_list in reader:
            key = row_list[key_column_index]
            name = row_list[NAME_INDEX]
            price = float(row_list[PRICE_INDEX])
            products_dict[key] = [key, name, price]
    return products_dict

def main():
    products_dict = read_dictionary("products.csv")
    print(products_dict)
    
    print("\nRequested Items")
    with open("request.csv", 'rt') as request_file:
        request_reader = csv.reader(request_file)
        next(request_reader)
        
        for row in request_reader:
            product_number = row[PRODUCT_INDEX]
            requested_quantity = int(row[1]) 
            
            product_info = products_dict.get(product_number)
            
            if product_info:
                product_name = product_info[1]
                product_price = product_info[2]
                print(f"{product_name}: {requested_quantity} @ {product_price:.2f}")
            else:
                print(f"Product with number {product_number} not found.")
                
if __name__ == "__main__":
    main()
