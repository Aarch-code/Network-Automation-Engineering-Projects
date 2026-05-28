"""Coding Challenge
1. Using requests connect to https://jsonplaceholder.typicode.com/users and take the JSON encoded string in Python object
2. The resulting Python object will be a list of dictionaries. Process the list and extract the following information for each user:
- Name
- City
- GPS coordinates in form of (LAT, LNG)
- Company's name the user is working for
3. Write to a CSV File a row for each user. The fields of the CSV file will be: name, city, GPS coordinates and company's name
For example for the first user you'll write in the CSV file: Leanne Graham,Gwenborough,"(-37.3159,-37.3159)",Romaguera-Crona"""

import requests
import csv

# 1. Get JSON data
response = requests.get('https://jsonplaceholder.typicode.com/users')

# convert JSON into Python object
users = response.json()

# 2 + 3. write required fields to csv
with open('users.csv', 'w', newline='') as f:
    writer = csv.writer(f)

    # optional header
    writer.writerow(['name', 'city', 'gps', 'company'])

    for user in users:

        name = user['name']

        city = user['address']['city']

        lat = user['address']['geo']['lat']
        lng = user['address']['geo']['lng']

        gps = f'({lat},{lng})'

        company = user['company']['name']

        writer.writerow([name, city, gps, company])

# read and print file
with open('users.csv') as f:
    print(f.read())