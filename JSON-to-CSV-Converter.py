# Python program to convert JSON file to CSV

from tkinter.filedialog import askopenfilename
import json
import csv

# ask user to select a JSON file
JSONfilePath = askopenfilename()
# Opening JSON file and loading the data into a variable
with open(JSONfilePath) as json_file:
    data = json.load(json_file)

# keeping the same path for the resulting CSV file
resultCSVpath = JSONfilePath.replace('.json', '.csv')

# creating a CSV file and writing the headers
with open(resultCSVpath, 'w') as csvfile:
    fieldnames = list(data[0].keys())
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for data in data:
        writer.writerow(data)

print("CSV file created successfully!")