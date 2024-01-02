#!/usr/bin/python3
"""Makes an API request and returns information about an employee's
TODO list progress
"""

if __name__ == '__main__':
    import json
    import requests
    from sys import argv

    EMPLOYEE_ID = argv[1]
    URL = 'https://jsonplaceholder.typicode.com/users'
    try:
        user = requests.get('{}/{}'.format(URL, EMPLOYEE_ID)).json()
        user_todos = requests.get('{}/{}/todos'.format(
            URL, EMPLOYEE_ID)).json()
        USER_ID = user.get('id')
        data = {}
        my_user = []
        for todo in user_todos:
            user_data = {
                "task": todo.get('title'),
                "completed": todo.get('completed'),
                "username": user.get('username'),
            }
            my_user.append(user_data)
        data.update({USER_ID: my_user})
        with open('{}.json'.format(USER_ID), 'w', encoding='utf-8') as f:
            json_data = json.dumps(data)
            f.write(json_data)
    except Exception as error:
        print(error)
