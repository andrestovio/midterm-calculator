"""
This file contains unit tests for the arithmetic functions in the operations module.
It uses pytest to validate the Addition, Subtraction, Multiplication, and Division functions,
including special handling for Division by zero to ensure error handling is correct.
"""

import pytest
from app.operations import addition, subtraction, multiplication, division

# Test for the Addition function
@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),         # Testing positive integers
    (1.5, 2.5, 4),     # Testing positive floats
    (-1, -2, -3),      # Testing negative integers
    (-1, 2, 1)         # Testing mixed sign integers
])
def test_addition(a, b, expected):
    """ Asserts that the Addition function returns the expected result for given inputs"""
    assert addition(a, b) == expected

# Test for the Subtraction function
@pytest.mark.parametrize("a, b, expected", [
    (3, 2, 1),         # Testing positive integers
    (5.5, 2.5, 3),     # Testing positive floats
    (-1, -2, 1),       # Testing negative integers
    (-1, 2, -3)        # Testing mixed sign integers
])
def test_subtraction(a, b, expected):
    """ Asserts that the Subtraction function returns the expected result for given inputs"""
    assert subtraction(a, b) == expected

# Test for the Multiplication function
@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 6),         # Testing positive integers
    (1.5, 2, 3),       # Testing positive float and integer
    (-1, -2, 2),       # Testing negative integers
    (-1, 2, -2)        # Testing mixed sign integers
])
def test_multiplication(a, b, expected):
    """ Asserts that the Multiplication function returns the expected result for given inputs"""
    assert multiplication(a, b) == expected

# Test for the Division function
@pytest.mark.parametrize("a, b, expected", [
    (6, 3, 2),         # Testing positive integers
    (5, 2, 2.5),       # Testing positive integer and float result
    (-6, -3, 2),       # Testing negative integers
    (-6, 3, -2)        # Testing mixed sign integers
])
def test_division(a, b, expected):
    """ Asserts that the Division function returns the expected result for given inputs"""
    assert division(a, b) == expected

# Test for Division by zero to ensure it raises a ValueError
@pytest.mark.parametrize("a, b", [
    (1, 0),            # Positive numerator, zero denominator
    (0, 0),            # Zero numerator, zero denominator
    (-1, 0),           # Negative numerator, zero denominator
])
def test_division_by_zero(a, b):
    """ Asserts that the Division function raises a ValueError with the expected message
    # when dividing by zero."""
    with pytest.raises(ValueError, match="Division by zero is not allowed."):
        division(a, b)
