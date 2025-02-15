import csv
from os import path
import re

FILE_DIR = path.dirname(path.realpath(__file__))
            
def read_dictionary(filename,index=0):
    """Read the contents of a CSV file into a
    dictionary and return the dictionary.
    Parameters
        filename: the name of the CSV file to read.
    Return: a dictionary that contains
        the contents of the CSV file.
    """
    students = {}
    with open(filename, "rt") as file_lines:
        reader = csv.reader(file_lines)
        next(reader)
        for line in reader:
            students[line[index]] = line[1]

        return students

def validate_number(number):
    if not re.match("^[\\d]{0,}$",number):
        raise Exception("Invalid I-Number")
            
    if len(number) < 9:
        raise Exception("Invalid I-Number: too few digits")
 
    if len(number) > 9:
        raise Exception("Invalid I-Number: too many digits")
       

def main():
    file = path.normpath('/'.join([FILE_DIR, "students.csv"]))
    students = read_dictionary(file)
    number = input("Give some Student I-Number: ")
    number = number.replace("-","")
    
    try:
        validate_number(number)
        print(students[number])
    except KeyError:
        print("No such student")
    except Exception as e:
        print(e)
 
if __name__ == "__main__":
    main()