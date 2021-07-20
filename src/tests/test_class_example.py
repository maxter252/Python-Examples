# Built-in library imports...
import unittest
from unittest.mock import Mock, patch

from src.classExample import Example
from src.constants import Config


class TestDataService(unittest.TestCase):
    @patch("src.classExample.Example.get_data")
    def test_class_example(self, mock_get_data):
        """Mock a function of a class"""
        mock_get_data.return_value = 5
        cle = Example()
        assert cle.get_data() == 5

    @patch("src.constants.Config.get_url")
    def test_mock_imported_class(self, mock_get_data):
        """Mock return value from a class function"""
        mock_get_data.return_value = "mocked_url!"
        cle = Example()
        assert cle.get_url() == "mocked_url!"

    # @patch('classExample.Example.get_object.return_value')
    # def test_mock_imported_class(self, mock):
    #     '''Mock only part of a return value from a class function'''
    #     mock.param1 = 'mocked_param'
    #     cle = Example()
    #     obj = cle.get_object()
    #     assert obj.param1 == 'mocked_param'
