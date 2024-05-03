import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    @parameterized.expand([
        ({}, ("a",), "Key 'a' not found in the map"),
        ({"a": 1}, ("a", "b"), "Key 'b' not found in the map"),
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected_message):
        with self.assertRaises(KeyError) as cm:
            access_nested_map(nested_map, path)
        self.assertEqual(str(cm.exception), expected_message)
