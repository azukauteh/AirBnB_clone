#!/usr/bin/python3
"""Defines unittests for console.py.

Unittest classes:
    TestHBNBCommand_setup
    TestHBNBCommand_create
    TestHBNBCommand_do
    TestHBNBCommand_create
    TestHBNBCommand_show
    TestHBNBCommand__all
    TestHBNBCommand_destroy
    TestHBNBCommand_update
    TesrHBNBCommand_count
"""
import unittest
import re
from io import StringIO
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models.base_model import BaseModel
from models.user import User


class TestHBNBCommand(unittest.TestCase):

    def setUp(self):
        self.console = HBNBCommand()
        self.mock_stdout = StringIO()

    def tearDown(self):
        self.console = None
        self.mock_stdout.close()

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_create(self, mock_stdout):
        self.console.do_create("BaseModel")
        output = mock_stdout.getvalue().strip()
        self.assertTrue(re.match(r"^[0-9a-f\-]{36}$", output))

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_show(self, mock_stdout):
        instance = BaseModel()
        self.console.do_show("BaseModel {}".format(instance.id))
        show_output = mock_stdout.getvalue().strip()
        self.assertIn(instance.__str__(), show_output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_all(self, mock_stdout):
        self.console.do_create("BaseModel")
        self.console.do_all("BaseModel")
        all_output = mock_stdout.getvalue().strip()
        self.assertIn("[BaseModel]", all_output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_destroy(self, mock_stdout):
        instance = BaseModel()
        self.console.do_destroy("BaseModel {}".format(instance.id))
        self.console.do_show("BaseModel {}".format(instance.id))
        show_output = mock_stdout.getvalue().strip()
        self.assertIn("** no instance found **", show_output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_update(self, mock_stdout):
        instance = BaseModel()
        self.console.do_update(f"BaseModel {instance.id} name 'new_name'")
        self.console.do_show("BaseModel {}".format(instance.id))
        show_output = mock_stdout.getvalue().strip()
        self.assertIn("'name': 'new_name'", show_output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_count(self, mock_stdout):
        self.console.do_create("BaseModel")
        self.console.do_count("BaseModel")
        count_output = mock_stdout.getvalue().strip()
        self.assertEqual(count_output, "i")


if __name__ == '__main__':
    unittest.main()
