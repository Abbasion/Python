import csv
reader = csv.reader(open("Book2.csv"))
for row in reader:
    print(row)