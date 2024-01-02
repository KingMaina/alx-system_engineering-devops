#!/usr/bin/python3
"""Makes an API request and returns information about all employee's
TODO list progress
"""

if __name__ == '__main__':
    import json
    import requests
    from sys import argv

    try:
        all_employees = {}
        for employee_id in range(1, 11):
            URL = 'https://jsonplaceholder.typicode.com/users'
            user = requests.get('{}/{}'.format(URL, employee_id)).json()
            user_todos = requests.get('{}/{}/todos'.format(
                URL, employee_id)).json()
            USER_ID = user.get('id')
            my_user = []
            for todo in user_todos:
                user_data = {
                    "username": user.get('username'),
                    "task": todo.get('title'),
                    "completed": todo.get('completed'),
                }
                my_user.append(user_data)
            all_employees.update({USER_ID: my_user})
        with open('todo_all_employees.json', 'w', encoding='utf-8') as f:
            json_data = json.dumps(all_employees)
            f.write(json_data)
    except Exception as error:
        print(error)
