# !#/usr/bin/python3
import csv
# importing element tree
# under the alias of ET
import xml.etree.ElementTree as ET

# tree = ET.parse('dict.xml')

with open('file.csv', mode='r') as csv_file:
    csv_reader = csv.reader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        print(f'\t{row["name"]} works in the {row["id"]} department, and was born in {row["year of birth"]}.')
        print(f'{row}')
        line_count += 1
    print(f'Processed {line_count} lines.')
