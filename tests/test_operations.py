"""
This file contains unit tests for the arithmetic functions in the operations module,
including both positive and negative test cases for addition, subtraction, multiplication,
and division functions.

The positive tests validate that each function produces correct results for a range of 
valid inputs, including positive numbers, negative numbers, and mixed-sign numbers.

The negative tests ensure that each function handles invalid inputs gracefully, such as
incorrect data types for addition and division by zero for the division function.

Each test case uses `pytest.mark.parametrize` for parameterized testing, and `pytest.raises`
to check for expected exceptions in the negative tests.
"""

import pytest
from app.operations import addition, subtraction, multiplication, division

# Positive test cases for arithmetic functions

# Positive test cases for the addition function
@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),         # Testing addition with positive integers
    (1.5, 2.5, 4),     # Testing addition with positive floats
    (-1, -2, -3),      # Testing addition with negative integers
    (-1, 2, 1)         # Testing addition with mixed sign integers
])
def test_addition_positive(a, b, expected):
    """Tests that the addition function returns the expected result for valid inputs."""
    assert addition(a, b) == expected

# Positive test cases for the subtraction function
@pytest.mark.parametrize("a, b, expected", [
    (3, 2, 1),         # Testing subtraction with positive integers
    (5.5, 2.5, 3),     # Testing subtraction with positive floats
    (-1, -2, 1),       # Testing subtraction with negative integers
    (-1, 2, -3)        # Testing subtraction with mixed sign integers
])
def test_subtraction_positive(a, b, expected):
    """Tests that the subtraction function returns the expected result for valid inputs."""
    assert subtraction(a, b) == expected

# Positive test cases for the multiplication function
@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 6),         # Testing multiplication with positive integers
    (1.5, 2, 3),       # Testing multiplication with a positive float and integer
    (-1, -2, 2),       # Testing multiplication with negative integers
    (-1, 2, -2)        # Testing multiplication with mixed sign integers
])
def test_multiplication_positive(a, b, expected):
    """Tests that the multiplication function returns the expected result for valid inputs."""
    assert multiplication(a, b) == expected

# Positive test cases for the division function
@pytest.mark.parametrize("a, b, expected", [
    (6, 3, 2),         # Testing division with positive integers
    (5, 2, 2.5),       # Testing division with a positive integer and float result
    (-6, -3, 2),       # Testing division with negative integers
    (-6, 3, -2)        # Testing division with mixed sign integers
])
def test_division_positive(a, b, expected):
    """Tests that the division function returns the expected result for valid inputs."""
    assert division(a, b) == expected


# Negative test cases for arithmetic functions

# Negative test cases for the addition function (e.g., invalid inputs)
@pytest.mark.parametrize("a, b, expected", [
    (1, None, TypeError),          # Testing addition with None
    ("1", 2, TypeError),           # Testing addition with a string and an integer
    ([1], 2, TypeError),           # Testing addition with a list and an integer
])
def test_addition_negative(a, b, expected):
    """Tests that the addition function raises the correct error for invalid inputs."""
    with pytest.raises(expected):
        addition(a, b)

# Negative test cases for the division function (division by zero)
@pytest.mark.parametrize("a, b", [
    (1, 0),            # Positive numerator, zero denominator
    (0, 0),            # Zero numerator, zero denominator
    (-1, 0),           # Negative numerator, zero denominator
])
def test_division_by_zero(a, b):
    """
    Tests that the division function raises a ValueError with the expected message 
    when dividing by zero.
    """
    with pytest.raises(ValueError, match="division by zero is not allowed."):
        division(a, b)
