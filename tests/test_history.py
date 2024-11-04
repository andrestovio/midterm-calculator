"""
This module contains test cases for the History class in the `app.history` module.
It uses pytest to validate the behavior of the add, get_history, undo_last, and clear
methods of the History class. The tests are organized into positive and negative cases
to ensure comprehensive coverage of both expected and edge case behaviors.

The test functions:
- `test_add_and_get_history_positive`: Tests adding operations to history and retrieving them.
- `test_undo_last_positive`: Tests undoing the last operation added to history.
- `test_history_negative`: Tests edge cases and incorrect usage of the History class, such as
  adding None and clearing the history.
"""

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