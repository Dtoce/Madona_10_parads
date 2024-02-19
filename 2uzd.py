import csv

def print_fourth_column(csv_file):
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) >= 4: 
                print(row[3])