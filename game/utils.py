import csv
import os

def append_to_csv(file_path, row_data, fieldnames):
    """Appends a row to a CSV file, writes headers if file is new/empty"""
    file_exists = os.path.isfile(file_path)
    
    with open(file_path, 'a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        if not file_exists or os.path.getsize(file_path) == 0:
            writer.writeheader()
        writer.writerow(row_data)
