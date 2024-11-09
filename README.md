Calculator REPL with History and Testing
Overview
This project is a command-line calculator with a Read-Eval-Print Loop (REPL) interface that supports basic arithmetic operations and advanced features such as modulus and exponentiation. The calculator can:

Perform basic operations: addition, subtraction, multiplication, and division.
Support modulus and exponentiation operations.
Manage calculation history with commands to view, clear, undo, save, and load history from a file.
The project includes a robust test suite using pytest to validate functionality, covering both positive and negative cases, with Pylint compliance for code quality.

Features
Basic Operations: Addition, subtraction, multiplication, and division.
Advanced Operations: Modulus and exponentiation.
History Management:
View history: Display all past calculations.
Clear history: Remove all records from history.
Undo: Remove the last calculation.
Save/Load: Save history to a CSV file and load it back.
Error Handling:
Handles invalid inputs, such as non-numeric inputs, unsupported operations, and division/modulus by zero.
calculator/
├── app/
│   ├── calculator.py          # Main calculator REPL logic
│   ├── operations.py          # Contains arithmetic functions (addition, subtraction, etc.)
│   ├── history.py             # History management (add, save, load, etc.)
│   └── logging.py             # Configures logging for the project
├── tests/
│   ├── test_calculator.py     # Tests for calculator REPL including command handling
│   ├── test_operations.py     # Tests for operations (addition, modulus, etc.)
│   └── test_history.py        # Tests for history functionality (save, load, undo, etc.)
├── .env                       # Environment variables (LOG_FILE, HISTORYCSV_FILE)
├── requirements.txt           # Project dependencies
└── README.md                  # Project documentation (this file)


Configure Environment Variables: Created a .env file in the project root with the following environment variables:
LOG_FILE=calculator.log
HISTORYCSV_FILE=default.csv
LOG_FILE specifies where logs are saved.
HISTORYCSV_FILE specifies the default file for saving/loading history

Usage
To start the calculator REPL, run the following command:
python -m app.calculator

Available Commands
Basic Arithmetic:

add <num1> <num2>: Adds two numbers.
subtract <num1> <num2>: Subtracts the second number from the first.
multiply <num1> <num2>: Multiplies two numbers.
divide <num1> <num2>: Divides the first number by the second (raises an error for division by zero).
Advanced Operations:

modulus <num1> <num2>: Calculates num1 % num2 (raises an error for modulus by zero).
exponent <num1> <num2>: Calculates num1 raised to the power of num2.
History Management:

history: Displays the calculation history.
clear: Clears the entire calculation history.
undo: Removes the last calculation from history.
save: Saves the current history to HISTORYCSV_FILE.
load: Loads history from HISTORYCSV_FILE.
Exit:

exit: Exits the calculator REPL.

Testing
The project includes a suite of tests using pytest to validate the functionality of the calculator, operations, and history management. Tests cover both positive and negative cases.

Run all tests with coverage
pytest --cov=app --pylint

Check Pylint Compliance: The code is Pylint-compliant, and you can view Pylint errors as part of the test suite using the command above.

Test Suite Structure
test_calculator.py: Tests the main calculator REPL, including command handling and history.
test_operations.py: Tests individual arithmetic operations (addition, subtraction, etc.).
test_history.py: Tests history management features, including save, load, undo, and error handling.

Logging
Logs are generated for key events in the calculator, such as:

User input
Calculation results
Errors (e.g., invalid input, division by zero)
Logs are saved to the file specified in the .env file under LOG_FILE

VIDEO LINK:
https://youtu.be/4tMNhhuWdZc

Andres Tovio Pabon