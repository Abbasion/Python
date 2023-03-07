import csv
print("Write dictionaries to a CSV file:")
fw = open('C:\\Users\\PC\\Documents\\GitHub\\Python\\Python built-in Modules\\Book2.csv', 'w', newline='')
writer = csv.DictWriter(fw,fieldnames=["Name","Class"])
writer.writeheader()
writer.writerow({"Name": "Jasmine Barrett", "Class": "V"})
writer.writerow({"Name": "Garry Watson", "Class": "V"})
writer.writerow({"Name": "Courtney Caldwell", "Class": "VI"})
fw.close()
fr = open('C:\\Users\\PC\\Documents\\GitHub\\Python\\Python built-in Modules\\Book2.csv', 'r')
csv = csv.reader(fr, delimiter= ",")
for row in csv:
    print(row)
fr.close()
