"""Challenge #1
Consider the following Python list:
people = [
['Dan', 34, 'Bucharest'],
['Andrei',21, 'London'],
['Maria', 45, 'Paris']
]
Using the CSV module write each element of the list (which is another list) into a CSV file called people1.csv
After writing into the file, read and print out the file contents.
Use the default , (comma) as the delimiter."""

import csv

people = [
    ['Dan', 34, 'Bucharest'],
    ['Andrei', 21, 'London'],
    ['Maria', 45, 'Paris']
]

with open('people1.csv', 'w', newline='') as f:
    writer = csv.writer(f)

    for person in people:
        writer.writerow(person)

with open('people1.csv', 'r') as f:
    content = f.read()
    print(content)        