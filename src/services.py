# Standard library imports...
import json
from urllib.parse import urljoin

# Third-party imports...
import requests

# Local imports...
from src.constants import Config

config = Config()
TODOS_URL = urljoin(config.BASE_URL, "todos")


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
# print(parse_response(get_todos()))
