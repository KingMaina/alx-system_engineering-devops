#!/usr/bin/python3
"""Makes an API request and returns information about an employee's
TODO list progress
"""

if __name__ == '__main__':
    import csv
    import requests
    from sys import argv

    EMPLOYEE_ID = argv[1]
    URL = 'https://jsonplaceholder.typicode.com/users'
    try:
        user = requests.get('{}/{}'.format(URL, EMPLOYEE_ID)).json()
        user_todos = requests.get('{}/{}/todos'.format(
            URL, EMPLOYEE_ID)).json()
        USER_ID = user.get('id')
        with open('{}.csv'.format(USER_ID), 'w', encoding='utf-8') as f:
            USER_NAME = user.get('username')
            writer = csv.writer(f, quoting=csv.QUOTE_ALL)
            for todo in user_todos:
                STATUS = todo.get('completed')
                TITLE = todo.get('title')
                data = [USER_ID, USER_NAME, STATUS, TITLE]
                writer.writerow(data)
    except Exception as error:
        pass
