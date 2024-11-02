"""
Tests for the calculator function, covering both positive and negative cases.

The positive tests validate that the calculator performs basic operations correctly
(addition, subtraction, multiplication, division) with valid inputs.

The negative tests check the calculator's error handling, ensuring it responds correctly
to invalid inputs such as non-numeric values, insufficient or excess arguments, unknown
operations, and division by zero.
Each test case uses `capsys` to capture output and `unittest.mock.patch` to simulate
user input.
"""

from unittest.mock import patch
import pytest
from app.calculator import calculator

# Positive test cases for the calculator function
@pytest.mark.parametrize("user_input, expected_output", [
    ("add 1 2", "Result: 3.0"),                    # Testing addition with positive integers
    ("subtract 5 3", "Result: 2.0"),                # Testing subtraction with positive integers
    ("multiply 4 3", "Result: 12.0"),               # Testing multiplication with positive integers
    ("divide 10 2", "Result: 5.0"),# Testing division with valid non-zero denominator
])
def test_calculator_positive_cases(user_input, expected_output, capsys):
    """
    Tests the calculator function with valid inputs to ensure correct results.
    Each case includes a valid operation and input numbers, checking if the
    expected result is printed.
    """
    # Patch 'input' to simulate user input and trigger calculator function
    with patch("builtins.input", side_effect=[user_input, "exit"]):
        calculator()  # Call the calculator function

        # Capture the output printed by the calculator function
        captured = capsys.readouterr()

        # Assert that the expected output matches the captured output
        assert expected_output in captured.out


# Negative test cases for the calculator function (including divide by zero)
@pytest.mark.parametrize("user_input, expected_output", [
    # Non-numeric input
    ("add a b",
     "Invalid input. Please follow the format: <operation> <num1> <num2>"),

    # Insufficient arguments
    ("add 1",
     "Invalid input. Please follow the format: <operation> <num1> <num2>"),

    # Excess arguments
    ("add 1 2 3",
     "Invalid input. Please follow the format: <operation> <num1> <num2>"),

    # Unknown operation
    ("unknown 1 2",
     "Unknown operation 'unknown'. Supported operations: add, subtract, multiply, divide."),

    # Division by zero case
    ("divide 10 0",
     "division by zero is not allowed.")
])

def test_calculator_negative_cases(user_input, expected_output, capsys):
    """
    Tests the calculator function with invalid inputs, including division by zero,
    to ensure that it handles errors properly.
    Each case checks if the correct error message is printed.
    """
    # Patch 'input' to simulate user input and trigger calculator function
    with patch("builtins.input", side_effect=[user_input, "exit"]):
        calculator()  # Call the calculator function

        # Capture the output printed by the calculator function
        captured = capsys.readouterr()

        # Assert that the expected error output matches the captured output
        assert expected_output in captured.out
