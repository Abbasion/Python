import csv
reader = csv.reader(open('C:\\Users\\PC\\Documents\\GitHub\\Python\\Python built-in Modules\\Book2.csv'))
no_lines = len(list(reader))
print(no_lines)