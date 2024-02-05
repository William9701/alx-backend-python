#!/usr/bin/env python3
"""This is a testing class"""
import unittest
from unittest.mock import Mock, patch

from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """this is the test class"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """the tset_access_nested method"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), "'a'"),
        ({"a": 1}, ("a", "b"), "'b'")
    ])
    def test_access_nested_map_exception(self, nested_map, path,
                                         expected_message):
        with self.assertRaises(KeyError) as cm:
            access_nested_map(nested_map, path)
        self.assertEqual(str(cm.exception), expected_message)


class TestGetJson(unittest.TestCase):
    """This clss tests the get_json method"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        """a mock method to actualize the test operation"""
        mock_get.return_value = Mock(json=lambda: test_payload)

        response = get_json(test_url)

        mock_get.assert_called_once_with(test_url)
        self.assertEqual(response, test_payload)


class TestClass:
    """Test class"""
    def a_method(self):
        return 42

    @memoize
    def a_property(self):
        return self.a_method()


class TestMemoize(unittest.TestCase):
    """Test class"""
    @patch.object(TestClass, 'a_method', return_value=42)
    def test_memoize(self, mock_a_method):
        """test memorize """
        test_obj = TestClass()
        # Call a_property twice
        res1 = test_obj.a_property
        res2 = test_obj.a_property

        # Check that the correct result is returned
        self.assertEqual(res1, 42)
        self.assertEqual(res2, 42)

        # Check that a_method is only called once
        mock_a_method.assert_called_once()
