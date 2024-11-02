import pytest
from unittest.mock import patch
from app.calculator import calculator

@pytest.mark.parametrize("user_input, expected_output", [
    ("add 1 2", "Result: 3.0\n"),
    ("subtract 5 3", "Result: 2.0\n"),
    ("multiply 4 3", "Result: 12.0\n"),
    ("divide 10 2", "Result: 5.0\n"),
    ("divide 10 0", "Division by zero is not allowed.\n"),
    ("unknown 1 2", "Unknown operation 'unknown'. Supported operations: add, subtract, multiply, divide.\n"),
    ("invalid input", "Invalid input. Please follow the format: <operation> <num1> <num2>\n"),
])
def test_calculator(user_input, expected_output, capsys):
    with patch("builtins.input", side_effect=[user_input, "exit"]):
        calculator()
        captured = capsys.readouterr()
        assert expected_output in captured.out
