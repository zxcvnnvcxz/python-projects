import csv

with open("Files/weather.csv", 'r') as file:
    data = list(csv.reader(file))

city = input("Enter a city: ")

for row in data[1:]:
    if row[0] == city:
        print("Temperature is " + row[1])
