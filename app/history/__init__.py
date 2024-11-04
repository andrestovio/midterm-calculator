class History:
    """
    A simple history tracker for a calculator that records every operation performed.

    Attributes:
        history (list): Stores each operation and its result as a string.

    Methods:
        add(operation: str): Adds a new operation to the history.
        get_history() -> list: Returns the list of all recorded operations.
        clear(): Clears all history entries.
        undo_last(): Removes the most recent entry from the history.
    """

    def __init__(self):
        """Initializes the History object with an empty history list."""
        # Initialize an empty list to store history of operations
        self.history = []

    def add(self, operation: str):
        """
        Adds a new operation to the history.

        Args:
            operation (str): A string representation of the operation, e.g., "add 2 + 3 = 5".

        Raises:
            TypeError: If the operation is not a string.
        """
        # Check if the operation is a string; if not, raise a TypeError
        if not isinstance(operation, str):
            raise TypeError("Operation must be a string.")
        
        # Append the operation string to the history list
        self.history.append(operation)

    def get_history(self) -> list:
        """
        Returns the list of all recorded operations.

        Returns:
            list: The list of all operations in the history.
        """
        # Return the entire list of operations
        return self.history

    def clear(self):
        """Clears all entries in the history."""
        # Clear the history list to remove all recorded operations
        self.history.clear()

    def undo_last(self):
        """
        Removes the most recent entry from the history.
        If history is empty, it does nothing.
        """
        # Remove the last entry from history if it exists
        if self.history:
            self.history.pop()
