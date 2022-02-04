#!/usr/bin/python3
"""
script that, for a given employee ID, returns information about his/her
"""
import requests
from sys import argv

if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/'
    req1 = requests.get(url + "users/" + argv[1])
    employee = req1.json().get("name")
    req2 = requests.get(url + 'todos?userId=' + argv[1]).json()
    completed_tasks = 0
    all_tasks = 0
    title = []
    if employee is not None:
        for i in req2:
            if i.get("completed") is True:
                completed_tasks += 1
                title.append(i.get("title"))
            all_tasks += 1
        print(
            "Employee {} is done with tasks({}/{}):"
            .format(employee, completed_tasks, all_tasks)
            )
        for j in title:
            print("\t {}".format(j))
