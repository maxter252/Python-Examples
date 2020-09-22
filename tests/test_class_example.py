# Built-in library imports...
from unittest.mock import Mock, patch
import unittest

from classExample import Example
from constants import Config


class TestDataService(unittest.TestCase):
    @patch('classExample.Example.get_data')
    def test_class_example(self, mock_get_data):
        mock_get_data.return_value = 5
        cle = Example()
        assert cle.get_data() == 5

    @patch('constants.Config.get_url')
    def test_mock_imported_class(self, mock_get_data):
        mock_get_data.return_value = 'mocked_url!'
        cle = Example()
        assert cle.get_url() == 'mocked_url!'