#!/usr/bin/python3
"""
export data in the CSV format
"""
import csv
import requests
from sys import argv

if __name__ == '__main__':
    arg = argv[1]
    url = "https://jsonplaceholder.typicode.com/users/" + arg
    user = requests.get(url, verify=False).json()
    url2 = "https://jsonplaceholder.typicode.com/todos?userId=" + arg
    data = requests.get(url2, verify=False).json()

    with open(arg + ".csv", 'w', newline='') as csv_file:
        archivo = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for i in data:
            archivo.writerow([int(arg), user.get('username'),
                             i.get('completed'),
                             i.get('title')])
