import csv
from urllib.request import urlretrieve 

file_name = "banklist.csv"
target_file = urlretrieve("https://s3.amazonaws.com/nicar17/pycar17/banklist.csv", file_name)

with open(file_name, "rU") as file:
    csv_data = csv.reader(file)
    
    for row in csv_data:
        
        print(row)
        print(type(row))