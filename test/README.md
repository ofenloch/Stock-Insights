# Unit Tests

This directory contains unit tests for the Stock-Insights project.

## Running Tests

Run all tests using Python's unittest module:

```bash
python3 -m unittest discover -s test -v
```

Or run a specific test file:

```bash
python3 -m unittest test.test_data_fetcher -v
```

Run a specific test class:

```bash
python3 -m unittest test.test_data_fetcher.TestSafeFloat -v
```

Run a specific test:

```bash
python3 -m unittest test.test_data_fetcher.TestSafeFloat.test_valid_float_string -v
```

## Test Structure

Tests are organized using Python's unittest framework, which is built-in and requires no additional dependencies.

### Example Test Class

```python
import unittest

class TestFeature(unittest.TestCase):
    """Test the feature function."""
    
    def test_basic_case(self):
        """Test basic functionality."""
        self.assertEqual(function_under_test("input"), "expected_output")
    
    def test_error_case(self):
        """Test error handling."""
        self.assertIsNone(function_under_test(None))
```

## Current Tests

- **test_data_fetcher.py** - Tests for utility functions in data_fetcher.py
  - `TestSafeFloat` - Tests for safe_float() function (converts strings to floats safely)
  - `TestSafeInt` - Tests for safe_int() function (converts strings to integers safely)

## Writing New Tests

1. Create a new test file: `test_<module_name>.py`
2. Import unittest and the module to test
3. Create test classes that inherit from `unittest.TestCase`
4. Write test methods starting with `test_`
5. Use assertions like `assertEqual`, `assertIsNone`, `assertTrue`, etc.

### Useful Assertions

- `assertEqual(a, b)` - Check if a equals b
- `assertIsNone(x)` - Check if x is None
- `assertTrue(x)` - Check if x is True
- `assertFalse(x)` - Check if x is False
- `assertRaises(Exception, func)` - Check if func raises Exception
- `assertIn(a, b)` - Check if a is in b

See [Python unittest documentation](https://docs.python.org/3/library/unittest.html) for more.
