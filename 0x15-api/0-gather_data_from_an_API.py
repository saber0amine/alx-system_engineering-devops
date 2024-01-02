#!/usr/bin/python3
"""request resource /users/:id & return info about the user"""
from requests import get
from sys import argv


if __name__ == '__main__':
    userId = argv[1]
    user = get("https://jsonplaceholder.typicode.com/users/{}"
               .format(userId))

    name = user.json().get('name')

    todos = get('https://jsonplaceholder.typicode.com/todos')
    totalTasks = 0
    done = 0

    for todo in todos.json():
        if todo.get('userId') == int(userId):
            totalTasks += 1
            if todo.get('completed'):
                done += 1

    print('Employee {} is done with tasks({}/{}):'
          .format(name, done, totalTasks))

    print('\n'.join(["\t " + task.get('title') for task in todos.json()
          if task.get('userId') == int(userId) and task.get('completed')]))
