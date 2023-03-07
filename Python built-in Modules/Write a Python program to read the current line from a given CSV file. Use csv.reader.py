import csv
f = open('C:\\Users\\PC\\Documents\\GitHub\\Python\\Python built-in Modules\\Book2.csv', newline='')
csv_reader = csv.reader(f)
print(next(csv_reader))
print(next(csv_reader))
print(next(csv_reader))