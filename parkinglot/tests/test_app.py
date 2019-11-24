import os
from io import StringIO
from unittest import TestCase
from unittest.mock import patch

import parkinglot
import parkinglot.app
from parkinglot.models import ParkingLot


def get_input(text):
    return input(text)


class AppTestCase(TestCase):
    """
    Test cases to for main script app.py
    """
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = dir_path + "/../../functional_spec/fixtures/file_input.txt"
    file_name = 'app.py'

    def setUp(self):
        """
        Make test database ready to run each test
        """
        ParkingLot.flush()

    def test_main_file_mode(self):
        parkinglot.app.main([self.file_path, self.file_path])

    def test_main_command_mode(self):
        cmd = 'exit'
        with patch('builtins.input', return_value=cmd), patch('sys.stdout', new=StringIO()):
            parkinglot.app.main([self.file_name])
