import csv
fw = open('C:\\Users\\PC\\Documents\\GitHub\\Python\\Python built-in Modules\\Book2.csv', 'w', newline='')
writer = csv.writer(fw, delimiter = ",")
writer.writerow(["a","b","c"])
writer.writerow(["d","e","f"])
writer.writerow(["g","h","i"])
fw.close()

fr = open('C:\\Users\\PC\\Documents\\GitHub\\Python\\Python built-in Modules\\Book2.csv','r')
csv = csv.reader(fr, delimiter= ",")
for row in csv:
    print(row)
fr.close()