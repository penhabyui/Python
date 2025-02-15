import csv
import math

NAME_INDEX = 0
SIZE_INDEX = 1
TIME_INDEX = 2

def main():
    products_dict = read_dictionary("cortecano.csv")
    for p in products_dict:
        print(p)
    
    part_name = input("What is the name of the part? ").lower()

    if part_name in products_dict:
        bar_length = 6000
        part_size = products_dict[part_name]['size']
        time_per_bar_minutes = products_dict[part_name]['time']

        pieces_per_bar = calculate_number_of_pieces(bar_length, part_size)
        print(f"We will get {pieces_per_bar:.2f} pieces per bar")

        desired_number_of_pieces = float(input("How many pieces are needed? "))
        required_bars = calculate_required_bars(desired_number_of_pieces, pieces_per_bar)
        print(f"To cut {desired_number_of_pieces} pieces we will need {required_bars} bars")

        total_time = calculate_total_time(required_bars, time_per_bar_minutes)
        
        if total_time < 60:
            print(f"Total time to cut {required_bars} bars: {total_time:.2f} minutes")
        else:
            hours = total_time // 60
            remaining_minutes = total_time % 60
            print(f"Total time to cut {required_bars} bars: {hours:.0f} hours and {remaining_minutes:.0f} minutes")
        
        remaining_length = calculate_remaining_length(bar_length, desired_number_of_pieces, part_size)
        print(f"After cutting {desired_number_of_pieces} pieces, {remaining_length} units of length remain in the bar.")
    else:
        print(f"The part '{part_name}' was not found in the CSV file.")

def read_dictionary(filename):
    products_dict = {}
    with open(filename, "rt") as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  
        for row in reader:
            name = row[NAME_INDEX].lower()
            size = float(row[SIZE_INDEX])
            time = float(row[TIME_INDEX])
            products_dict[name] = {'size': size, 'time': time}
    return products_dict

def calculate_number_of_pieces(bar_length, part_size):
    pieces_per_bar = bar_length // part_size  # Use integer division
    return pieces_per_bar

def calculate_required_bars(desired_number_of_pieces, pieces_per_bar):
    required_bars = math.ceil(desired_number_of_pieces / pieces_per_bar)
    return required_bars

def calculate_total_time(required_bars, time_per_bar_minutes):
    total_time = required_bars * time_per_bar_minutes
    return total_time

def calculate_remaining_length(bar_length, number_of_pieces, part_size):
    total_length_used = number_of_pieces * part_size
    remaining_length = bar_length - total_length_used

    if remaining_length < 0:
        remaining_length = 0
    
    return remaining_length

if __name__ == "__main__":
    main()
