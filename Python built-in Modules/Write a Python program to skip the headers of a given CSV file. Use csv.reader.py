import csv
f = open('C:\\Users\\PC\\Documents\\GitHub\\Python\\Python built-in Modules\\Book2.csv', newline='')
reader = csv.reader(f)
next(reader)

for row in reader:
    print(row)