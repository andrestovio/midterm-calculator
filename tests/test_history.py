"""
This module contains test cases for the History class in the `app.history` module.
It uses pytest to validate the behavior of the add, get_history, undo_last, clear,
save, and load methods of the History class. The tests are organized into positive
and negative cases to ensure comprehensive coverage of both expected and edge case
behaviors.

Test functions:
- `test_add_and_get_history_positive`: Tests adding operations to history and
  retrieving them.
- `test_undo_last_positive`: Tests undoing the last operation added to history.
- `test_save_and_load_history_positive`: Tests saving history to and loading it from
  a CSV file.
- `test_history_negative`: Tests edge cases and incorrect usage of the History class,
  such as adding None and clearing the history.
"""

import pandas as pd
import pytest
from app.history import History

# Positive test cases for the History class

@pytest.mark.parametrize("operations, expected_history", [
    (["add 2 + 3 = 5"], ["add 2 + 3 = 5"]),  # Single operation
    (["add 2 + 3 = 5", "multiply 4 * 5 = 20"],
     ["add 2 + 3 = 5", "multiply 4 * 5 = 20"]),  # Multiple operations
    ([], []),  # Empty history
])
def test_add_and_get_history_positive(operations, expected_history):
    """
    Tests that the History class correctly records and retrieves operations.

    Args:
        operations (list): List of operations to add to history.
        expected_history (list): Expected list of recorded operations.
    """
    # Create a History object
    history = History()

    # Add each operation to history
    for operation in operations:
        history.add(operation)

    # Assert that the history matches the expected history
    assert history.get_history() == expected_history


@pytest.mark.parametrize("initial_operations, expected_history", [
    (["add 2 + 3 = 5", "multiply 4 * 5 = 20"], ["add 2 + 3 = 5"]),  # Undo one operation
    (["add 2 + 3 = 5"], []),                                        # Undo single operation
    ([], []),                                                       # Undo on empty history
])
def test_undo_last_positive(initial_operations, expected_history):
    """
    Tests that the undo_last method removes the most recent operation from history.

    Args:
        initial_operations (list): List of initial operations to add to history.
        expected_history (list): Expected list of operations after undoing the last one.
    """
    # Create a History object
    history = History()

    # Add initial operations to history
    for operation in initial_operations:
        history.add(operation)

    # Undo the last operation
    history.undo_last()

    # Assert that the remaining history matches the expected history
    assert history.get_history() == expected_history


# Positive test cases for save and load functionality
@pytest.mark.parametrize("operations", [
    (["add 2 + 3 = 5", "multiply 4 * 5 = 20"]),
    (["add 10 + 15 = 25"]),
    ([]),  # Empty history case
])
def test_save_and_load_history_positive(operations, tmp_path):
    """
    Tests the save and load methods of the History class with different operations.

    Args:
        operations (list): List of operations to add to history before saving.
        tmp_path (path): Temporary directory provided by pytest for file operations.
    """
    # Create a History object and add operations
    history = History()
    for operation in operations:
        history.add(operation)

    # Define a temporary file path for saving and loading
    file_path = tmp_path / "test_history.csv"

    # Save the history to a CSV file
    history.save(file_path)

    # Create a new History object to load data
    new_history = History()
    new_history.load(file_path)

    # Assert that the loaded history matches the original operations
    assert new_history.get_history() == operations


# Negative test cases for the History class
@pytest.mark.parametrize("initial_operations, action, expected_exception", [
    (None, "add", TypeError),               # Adding None should raise TypeError
    ([], "undo_last", None),                # Undoing on empty history should not raise an error
    (["add 2 + 3 = 5"], "clear", None),     # Clearing should not raise an error
])
def test_history_negative(initial_operations, action, expected_exception):
    """
    Tests that the History class handles incorrect usage and edge cases properly.

    Args:
        initial_operations (list): List of operations to initialize in history.
        action (str): Action to perform ('add', 'undo_last', or 'clear').
        expected_exception (Exception or None): Expected exception type if any, else None.
    """
    # Create a History object
    history = History()

    # Populate the history if initial_operations is provided and is a list
    if isinstance(initial_operations, list):
        for operation in initial_operations:
            history.add(operation)
    elif initial_operations is None and action == "add" and expected_exception:
        # If initial_operations is None, test adding None and expect a TypeError
        with pytest.raises(expected_exception):
            history.add(None)
        return  # Exit the test early after raising the expected exception

    # Perform the specified action without expecting exceptions
    if action == "undo_last":
        # Undo the last operation; should not raise any error even if history is empty
        history.undo_last()
        # Confirm that history remains empty after calling undo on an empty history
        assert not history.get_history()

    elif action == "clear":
        # Clear the history, which should not raise any error
        history.clear()
        # Confirm that the history is empty after clearing
        assert not history.get_history()


# Negative test cases for save and load functionality
@pytest.mark.parametrize("file_path, expected_message", [
    ("non_existent_file.csv", "No file found at"),
    ("incorrect_format.csv", "CSV file does not contain 'Operation' column."),
])
def test_load_history_negative(file_path, expected_message, tmp_path, capsys):
    """
    Tests the load method of the History class with incorrect file paths or formats.

    Args:
        file_path (str): Path to the CSV file to load history from.
        expected_message (str): Expected message if loading fails.
        tmp_path (path): Temporary directory provided by pytest for file operations.
        capsys (CaptureFixture): Pytest fixture to capture stdout.
    """
    # Create a History object
    history = History()

    # Set up paths for testing file not found and incorrect format
    if file_path == "incorrect_format.csv":
        # Create an incorrect CSV file without 'Operation' column
        incorrect_path = tmp_path / file_path
        pd.DataFrame({"WrongColumn": ["data"]}).to_csv(incorrect_path, index=False)
        file_path = incorrect_path
    else:
        # Set file path to non-existent file for testing file not found
        file_path = tmp_path / file_path

    # Load the history from the specified file path
    history.load(file_path)

    # Capture the output and check for the expected message
    captured = capsys.readouterr()
    assert expected_message in captured.out
