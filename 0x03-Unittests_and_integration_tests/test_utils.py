#!/usr/bin/env python3
""" Unittests for utils.py """
import unittest
from unittest.mock import Mock, patch
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    ''' class to test access_nested_map function '''
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        ''' test access_nested_map function '''
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        ''' test that exception raises KeyErro'''
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)

class TestGetJson(unittest.TestCase):
    ''' class to test the get_json function '''
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        ''' tests the get_json function'''
        class Mocked(Mock):
            ''' A mock class representation'''

            def json(self):
                ''' json method mock'''
                return test_payload

        with patch('requests.get') as MockClass:
            MockClass.return_value = Mocked()
            self.assertEqual(get_json(test_url), test_payload)

class TestMemoize(unittest.TestCase):
    ''' test class for the memoize function '''

    def test_memoize(self):
        ''' tests the memoize function '''

        class TestClass:
            ''' lets mock '''

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mock_method:
            spec = TestClass()
            spec.a_property
            spec.a_property
            mock_method.assert_called_once()
