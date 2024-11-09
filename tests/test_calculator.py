"""
Tests for the calculator function, covering both positive and negative cases.

The positive tests validate that the calculator performs basic operations correctly
and includes tests for the history management commands (history, clear, undo, save).

The negative tests check the calculator's error handling for invalid inputs, such as
non-numeric values, unsupported operations, and history commands on an empty history.

Each test case uses `capsys` to capture output and `unittest.mock.patch` to simulate
user input.
"""

from unittest.mock import patch
import pytest
from app.calculator import calculator


# Positive test cases for the calculator function, including history management
@pytest.mark.parametrize("user_inputs, expected_outputs", [
    # Test basic calculation with history command
    (["add 1 2", "history", "exit"],
     ["Result: 3.0", "Calculation History:", "add 1.0 2.0 = 3.0"]),

    # Test clearing the history after a calculation
    (["add 1 2", "clear", "history", "exit"],
     ["Result: 3.0", "History cleared.", "Calculation History:"]),

    # Test undoing the last calculation
    (["multiply 4 5", "undo", "history", "exit"],
     ["Result: 20.0", "Last calculation undone.", "Calculation History:"]),

    # Test multiple entries and checking history
    (["add 1 2", "subtract 5 3", "multiply 2 3", "history", "exit"],
     ["Result: 3.0", "Result: 2.0", "Result: 6.0", "Calculation History:",
      "add 1.0 2.0 = 3.0", "subtract 5.0 3.0 = 2.0", "multiply 2.0 3.0 = 6.0"]),

    # Test history after multiple undo operations
    (["add 1 2", "subtract 4 2", "undo", "undo", "history", "exit"],
     ["Result: 3.0", "Result: 2.0", "Last calculation undone.",
      "Last calculation undone.", "Calculation History:"]),

    # Test saving and loading the history
    (["add 10 20", "save", "clear", "load", "history", "exit"],
     ["Result: 30.0", "History cleared.", "History saved to default.csv",
      "History loaded from default.csv", "Calculation History:", "add 10.0 20.0 = 30.0"]),
])
def test_calculator_positive_history_cases(user_inputs, expected_outputs, capsys):
    """
    Tests the calculator function with valid inputs and history management commands
    to ensure correct results and proper history handling.
    """
    # Patch 'input' to simulate user input and trigger the calculator function
    with patch("builtins.input", side_effect=user_inputs):
        calculator()  # Call the calculator function

        # Capture the output printed by the calculator function
        captured = capsys.readouterr()

        # Assert that each expected output is in the captured output
        for expected_output in expected_outputs:
            assert expected_output in captured.out


# Negative test cases for the calculator function's history management and error handling
@pytest.mark.parametrize("user_inputs, expected_outputs", [
    # Check undo with an empty history
    (["undo", "exit"],
     ["Last calculation undone."]),

    # Check history with an empty history
    (["history", "exit"],
     ["Calculation History:"]),

    # Check clear on empty history
    (["clear", "history", "exit"],
     ["History cleared.", "Calculation History:"]),

    # Check mix of commands with empty history
    (["clear", "undo", "history", "exit"],
     ["History cleared.", "Last calculation undone.", "Calculation History:"]),

    # Test invalid operation name
    (["unknown 1 2", "exit"],
     ["Unknown operation 'unknown'. Supported operations: add, subtract, "
      "multiply, divide."]),

    # Test division by zero
    (["divide 10 0", "exit"],
     ["division by zero is not allowed."]),

    # Test non-numeric input
    (["add a b", "exit"],
     ["Invalid input. Please follow the format: <operation> <num1> <num2>"]),

    # Test insufficient arguments
    (["add 1", "exit"],
     ["Invalid input. Please follow the format: <operation> <num1> <num2>"]),

    # Test excess arguments
    (["add 1 2 3", "exit"],
     ["Invalid input. Please follow the format: <operation> <num1> <num2>"]),

    # Test saving history with no calculations
    (["clear", "save", "history", "exit"],
     ["History cleared.", "History saved to default.csv", "Calculation History:"]),

    # Test loading history when "default.csv" is empty
    (["clear", "save", "load", "history", "exit"],
    ["History cleared.", "History saved to default.csv",
      "History loaded from default.csv", "Calculation History:"]),])
def test_calculator_negative_cases(user_inputs, expected_outputs, capsys):
    """
    Tests the calculator function with invalid inputs and history management commands,
    ensuring it handles errors and empty history properly.
    """
    # Patch 'input' to simulate user input and trigger the calculator function
    with patch("builtins.input", side_effect=user_inputs):
        calculator()  # Call the calculator function

        # Capture the output printed by the calculator function
        captured = capsys.readouterr()

        # Assert that each expected output is in the captured output
        for expected_output in expected_outputs:
            assert expected_output in captured.out
