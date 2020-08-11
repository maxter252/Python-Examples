# Standard library imports...
from unittest.mock import Mock, patch
import unittest

# Third-party imports...
import responses
import requests
import pytest

# Local imports...
from services import parse_response, get_todos

# Fixtures

# @pytest.fixture
def sample_api_response():
    return {'userId': 1, 'id': 1, 'title': 'delectus aut autem', 'completed': False}

# Tests
def test_always_passes():
    assert True

# @patch("project.services.get_todos.elem_1")
def test_request_response(): # mock_get

    # mock_get.return_value.ok = True
    # mock_elem_1 = 

    # Call the service, which will send a request to the server.
    output = parse_response(sample_api_response())

    # If the request is sent successfully, then I expect a response to be returned.
    assert output is not None
    assert output == 1


@patch('services.requests.get')
def test_integration(mock_requests):
    mock_requests.return_value.ok = True
    mock_requests.return_value.text = "response text"
    mock_requests.return_value.json.return_value = [{'userId': 1, 'id': 1, 'title': 'delectus aut autem', 'completed': False}]
    output = parse_response(get_todos(1))
    assert output == 1


# @responses.activate
# def test_simple():
#     responses.add(responses.GET, 'http://twitter.com/api/1/foobar',
#                   json={'error': 'not found'}, status=404)

#     resp = requests.get('http://twitter.com/api/1/foobar')

#     assert resp.json() == {"error": "not found"}


# def test_request_response_no_mock():

#     # Call the service, which will send a request to the server.
#     response = get_todos()

#     print("response ---->>>>> " + response.json)

#     # If the request is sent successfully, then I expect a response to be returned.
#     assert_is_not_none(response)