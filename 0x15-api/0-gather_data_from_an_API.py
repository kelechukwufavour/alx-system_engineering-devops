#!/usr/bin/python3
"""
Python script to fetch and display employee TODO list progress
"""

import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) != 2 or not argv[1].isdigit():
        print("Usage: {} employee_id".format(argv[0]))
        exit(1)

    employee_id = int(argv[1])
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    todos_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(employee_id)

    try:
        user_response = requests.get(user_url)
        todos_response = requests.get(todos_url)
        user_data = user_response.json()
        todos_data = todos_response.json()

        completed_tasks = [task for task in todos_data if task['completed']]
        total_tasks = len(todos_data)

        print("Employee {} is done with tasks({}/{}):".format(
            user_data['name'], len(completed_tasks), total_tasks
        ))

        for task in completed_tasks:
            print("\t {}".format(task['title']))

    except Exception as e:
        print("An error occurred: {}".format(e))
