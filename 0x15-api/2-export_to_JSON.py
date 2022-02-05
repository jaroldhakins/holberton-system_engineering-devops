#!/usr/bin/python3
'''
Inserts data in a json file
'''

import json
import requests
from sys import argv

if __name__ == '__main__':
    arg = argv[1]
    url = "https://jsonplaceholder.typicode.com/users/" + arg
    user = requests.get(url, verify=False).json()
    url2 = "https://jsonplaceholder.typicode.com/todos?userId=" + arg
    data = requests.get(url2, verify=False).json()
    my_dict = {}

    i = [{"task": i.get("title"), "completed": i.get("completed"),
          "username": user.get("username")} for i in data]

    my_dict[arg] = i

    with open(arg + ".json", "w") as json_file:
        json.dump(my_dict, json_file)
