import csv
with open("music.csv", "r") as c:
    csv_reader = csv.reader(c)
    for line in csv_reader:
        print(line)