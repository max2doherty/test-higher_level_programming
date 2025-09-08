#!/usr/bin/python3
"""Unittests for max_integer([..])."""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Unittests for max_integer."""

    def test_ordered_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_single_element_list(self):
        self.assertEqual(max_integer([7]), 7)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -5, -3]), -1)

    def test_mixed_numbers(self):
        self.assertEqual(max_integer([-10, 5, 3, -2]), 5)

    def test_floats(self):
        self.assertEqual(max_integer([1.5, 2.7, 0.3]), 2.7)

    def test_string(self):
        self.assertEqual(max_integer("abc"), "c")

    def test_list_of_strings(self):
        self.assertEqual(max_integer(["apple", "banana", "cherry"]), "cherry")

    def test_none_input(self):
        with self.assertRaises(TypeError):
            max_integer(None)


if __name__ == '__main__':
    unittest.main()