"""Challenge #2
Change the solution from the previous challenge and use : (colon) as the delimiter."""

import csv

people = [
    ['Dan', 34, 'Bucharest'],
    ['Andrei', 21, 'London'],
    ['Maria', 45, 'Paris']
]

with open('people2.csv', 'w', newline='') as f:
    writer = csv.writer(f, delimiter=':')

    for person in people:
        writer.writerow(person)

with open('people2.csv', 'r') as f:
    content = f.read()
    print(content)   