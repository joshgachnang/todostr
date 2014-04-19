import argparse
import json

import requests


class Client(object):
    def __init__(self, server_address="127.0.0.1:8000", username="",
                 password="", api_version=1):
        self.server_address = server_address
        self.api_version = api_version
        self.username = username
        self.password = password

    def _get_base_url(self):
        return "http://{}/api/v{}/".format(self.server_address.rstrip('/'),
                                           self.api_version)

    def post_to_server(self, path, payload):
        headers = {'content-type': 'application/json'}
        url = "{}{}".format(self._get_base_url(), path)
        return requests.post(url,
                             data=json.dumps(payload),
                             headers=headers,
                             auth=(self.username, self.password))

    def get_tasks(self):
        url = "{}{}".format(self._get_base_url(), 'tasks/')
        r = requests.get(url)
        tasks = []
        print "raw return", r.json()
        for task in r.json():
            tasks.append(Task.from_json(task))

        return tasks

    def add_task(self, args):
        url = "{}{}".format(self._get_base_url(), 'tasks/')
        payload = {
            'title': args,
        }
        response = self.post_to_server(path='tasks/', payload=payload)
        print response.json()

    def do_task(self, args):
        pass

    def describe_task(self, args):
        pass


class Task(object):
    def __init__(self, title,  description=None, due_date=None):
        self.title = title
        self.description = description
        self.due_date = due_date

    @classmethod
    def from_json(cls, data):
        return cls(title=data['title'],
                   description=data.get('title'),
                   due_date=data.get('due_date'))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Todostr todo list client')
    parser.add_argument('command', type=str, action='store', nargs='?',
                        default='list', help='The command to run. Can be one '
                                             'of "a/add", "d/do", '
                                             '"description".')
    parser.add_argument('args', type=str, nargs='*')
    args = parser.parse_args()

    client = Client(username='josh', password='password')

    if args.command == 'list':
        client.get_tasks()
    elif args.command in ['a', 'add']:
        client.add_task(args.args)
    elif args.command in ['d', 'do']:
        client.do_task(args.args)
    elif args.command in ['description']:
        client.describe_task(args.args)
