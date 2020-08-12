# Built-in library imports...
from unittest.mock import Mock, patch
import unittest

# Third-party imports...
import responses
import requests
import pytest

# Local imports...
from services import parse_response, get_todos

def sample_api_response():
    return {'userId': 1, 'id': 1, 'title': 'delectus aut autem', 'completed': False}

# ----- Tests ------ #
def test_always_passes():
    assert True
    
def test_request_response(): 
    'Test the parsing of the api response'
    # Call the service, which will send a request to the server.
    output = parse_response(sample_api_response())

    # If the request is sent successfully, then I expect a response to be returned.
    assert output is not None
    assert output == 1

@patch('services.requests.get')
def test_integration(mock_requests):
    'Test to show how to mock an api call'
    mock_requests.return_value.ok = True
    mock_requests.return_value.text = "response text"
    mock_requests.return_value.json.return_value = [{'userId': 1, 'id': 1, 'title': 'delectus aut autem', 'completed': False}]
    output = parse_response(get_todos(1))
    assert output == 1
