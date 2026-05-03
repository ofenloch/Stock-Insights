"""
Unit tests for data_fetcher module.
Tests utility functions for safe type conversion.


Run all tests:
    python3 -m unittest discover -s test -v

Run specific test file:
    python3 -m unittest test.test_data_fetcher -v

Run specific test class:
    python3 -m unittest test.test_data_fetcher.TestSafeFloat -v

"""
import math
import sys
import unittest
from pathlib import Path
from unittest import mock


# Mock database modules before importing data_fetcher
sys.modules['psycopg2'] = mock.MagicMock()
sys.modules['yfinance'] = mock.MagicMock()

from data_fetcher import safe_float, safe_int


class TestSafeFloat(unittest.TestCase):
    """Test the safe_float function."""

    def test_valid_float_string(self):
        """Test converting a valid float string."""
        self.assertEqual(safe_float("3.14"), 3.14)

    def test_valid_integer_string(self):
        """Test converting an integer string to float."""
        self.assertEqual(safe_float("42"), 42.0)

    def test_negative_float(self):
        """Test converting a negative float string."""
        self.assertEqual(safe_float("-2.5"), -2.5)

    def test_zero_float(self):
        """Test converting zero."""
        self.assertEqual(safe_float("0"), 0.0)

    def test_scientific_notation(self):
        """Test scientific notation."""
        self.assertEqual(safe_float("1e-3"), 0.001)

    def test_invalid_string_returns_none(self):
        """Test that invalid strings return None."""
        self.assertTrue(math.isnan(safe_float("invalid")))
        self.assertTrue(math.isnan(safe_float("abc123")))

    def test_empty_string_returns_none(self):
        """Test that empty string returns None."""
        self.assertTrue(math.isnan(safe_float("")))

    def test_none_input_returns_none(self):
        """Test that None input returns None."""
        self.assertTrue(math.isnan(safe_float(None)))

    def test_whitespace_string(self):
        """Test string with only whitespace."""
        self.assertTrue(math.isnan(safe_float("   ")))


class TestSafeInt(unittest.TestCase):
    """Test the safe_int function."""

    def test_valid_integer_string(self):
        """Test converting a valid integer string."""
        self.assertEqual(safe_int("42"), 42)

    def test_valid_float_string(self):
        """Test converting a float string to integer (should truncate)."""
        self.assertEqual(safe_int("3.14"), 3)

    def test_negative_integer(self):
        """Test converting a negative integer string."""
        self.assertEqual(safe_int("-10"), -10)

    def test_zero(self):
        """Test converting zero."""
        self.assertEqual(safe_int("0"), 0)

    def test_large_number(self):
        """Test converting a large number."""
        self.assertEqual(safe_int("999999999"), 999999999)

    def test_invalid_string_returns_zero(self):
        """Test that invalid strings return 0."""
        self.assertTrue(math.isnan(safe_int("invalid")))
        self.assertTrue(math.isnan(safe_int("abc123")))

    def test_empty_string_returns_zero(self):
        """Test that empty string returns 0."""
        self.assertTrue(math.isnan(safe_int("")))

    def test_none_input_returns_zero(self):
        """Test that None input returns 0."""
        self.assertTrue(math.isnan(safe_int(None)))

    def test_whitespace_string_returns_zero(self):
        """Test string with only whitespace returns 0."""
        self.assertTrue(math.isnan(safe_int("   ")))

if __name__ == "__main__":
    unittest.main(verbosity=2)
