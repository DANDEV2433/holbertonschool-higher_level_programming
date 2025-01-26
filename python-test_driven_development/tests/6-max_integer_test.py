#!/usr/bin/python3
"""
module test Function to find and return the max integer in a list of integers
        If the list is empty, the function returns None
"""
# import de la fonction
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    # Test for find the max_integer in list of number
    def test_integers(self):
        self.assertEqual(max_integer([1, 3, 12, 64]), 64)

    # Test with one argument
    def test_one_element(self):
        self.assertEqual(max_integer([42]), 42)

    # Test with negative numbers
    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -3, -12, -64]), -1)

    # Test with negative and positive numbers
    def test_mixed_numbers(self):
        self.assertEqual(max_integer([1, -3, 12, 64, 0]), 64)

    # Test in empty list
    def test_empty_list(self):
        self.assertIsNone(max_integer([]))


if __name__ == "__main__":
    unittest.main()
