# Standard library imports...
try:
    from urllib.parse import urljoin
except ImportError:
    from urlparse import urljoin

import json

# Third-party imports...
import requests

# Local imports...
from constants import BASE_URL

TODOS_URL = urljoin(BASE_URL, 'todos')


def get_todos(i):
    response = requests.get(TODOS_URL)
    json_resp = response.json()
    if response.ok:
        return json_resp[0]
    else:
        return None

def parse_response(res):
    return res["userId"]

def get_group_of_resp():
    result = []
    for i in [1]:
        item_id = parse_response(get_todos(i))  
        result.append(item_id)

# if __name__ == "main":
#print(parse_response(get_todos()))