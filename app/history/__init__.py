import pandas as pd

class History:
    """
    A simple history tracker for a calculator that records every operation 
    performed.

    Attributes:
        history (list): Stores each operation and its result as a string.

    Methods:
        add(operation: str): Adds a new operation to the history.
        get_history() -> list: Returns the list of all recorded operations.
        clear(): Clears all history entries.
        undo_last(): Removes the most recent entry from the history.
        save(file_path: str): Saves the history to a CSV file.
        load(file_path: str): Loads history from a CSV file.
    """

    def __init__(self):
        """Initializes the History object with an empty history list."""
        self.history = []

    def add(self, operation: str):
        """
        Adds a new operation to the history.

        Args:
            operation (str): A string representation of the operation, 
            e.g., "add 2 + 3 = 5".

        Raises:
            TypeError: If the operation is not a string.
        """
        if not isinstance(operation, str):
            raise TypeError("Operation must be a string.")
        
        self.history.append(operation)

    def get_history(self) -> list:
        """
        Returns the list of all recorded operations.

        Returns:
            list: The list of all operations in the history.
        """
        return self.history

    def clear(self):
        """Clears all entries in the history."""
        self.history.clear()

    def undo_last(self):
        """
        Removes the most recent entry from the history.
        If history is empty, it does nothing.
        """
        if self.history:
            self.history.pop()

    def save(self, file_path: str):
        """
        Saves the history to a CSV file.

        Args:
            file_path (str): The path to the CSV file where the history 
            will be saved.
        """
        df = pd.DataFrame(self.history, columns=["Operation"])
        df.to_csv(file_path, index=False)
        print(f"History saved to {file_path}")

    def load(self, file_path: str):
        """
        Loads history from a CSV file and populates the history list.

        Args:
            file_path (str): The path to the CSV file from which the history 
            will be loaded.
        """
        try:
            df = pd.read_csv(file_path)
            if 'Operation' in df.columns:
                self.history = df['Operation'].tolist()
                print(f"History loaded from {file_path}")
            else:
                print("CSV file does not contain 'Operation' column.")
        except FileNotFoundError:
            print(f"No file found at {file_path}")
