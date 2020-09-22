# Built-in library imports...
from unittest.mock import Mock, patch
import unittest

from classExample import Example

@patch('classExample.Example.get_data')
class TestDataService(unittest.TestCase):
    def test_class_example(self, mock_get_data):
        mock_get_data.return_value = 5
        cle = Example()
        assert cle.get_data() == 5