"""
A simple calculator REPL that can perform addition, subtraction, multiplication, and division.
The calculator includes a history feature allowing users to view past calculations, clear history,
and undo the last calculation.
"""

# Import the necessary math operations from the operations module
from app.operations import addition, subtraction, multiplication, division

# Import History class from the history module
from app.history import History


def calculator():
    """
    Basic REPL calculator that performs addition, subtraction, multiplication, and division,
    with support for viewing, clearing, and undoing calculation history.
    """
    # Display welcome message and instructions for using the calculator
    print("Welcome to the calculator REPL! Type 'exit' anytime to quit.")
    
    # Create a History object to manage the history of calculations
    history = History()

    # Start the REPL loop
    while True:
        # Prompt the user for an operation or command
        user_input = input("Enter an operation (add, subtract, multiply, divide) and two numbers, "
                           "or a command (history, clear, undo): ")

        # Handle the 'exit' command to quit the calculator
        if user_input.lower() == "exit":
            print("Exiting calculator...")
            break

        # Handle the 'history' command to display all past calculations
        elif user_input.lower() == "history":
            print("Calculation History:")
            for calc in history.get_history():
                print(calc)
            continue

        # Handle the 'clear' command to remove all history entries
        elif user_input.lower() == "clear":
            history.clear()
            print("History cleared.")
            continue

        # Handle the 'undo' command to remove the last calculation
        elif user_input.lower() == "undo":
            history.undo_last()
            print("Last calculation undone.")
            continue

        # Process the input as a calculation if it is not a command
        else:
            try:
                # Split the input into operation and numbers
                operation, num1, num2 = user_input.lower().split()
                num1, num2 = float(num1), float(num2)  # Convert numbers to float for calculations
            except ValueError:
                # Print error if input format is incorrect
                print("Invalid input. Please follow the format: <operation> <num1> <num2>")
                continue

            # Perform the requested operation and calculate the result
            if operation == "add":
                result = addition(num1, num2)
            elif operation == "subtract":
                result = subtraction(num1, num2)
            elif operation == "multiply":
                result = multiplication(num1, num2)
            elif operation == "divide":
                try:
                    result = division(num1, num2)
                except ValueError as error:
                    # Print error if division by zero is attempted
                    print(error)
                    continue
            else:
                # Print error if the operation is not recognized
                print(f"Unknown operation '{operation}'. Supported operations: add, subtract, multiply, divide.")
                continue

            # Store the calculation in the history
            calculation_str = f"{operation} {num1} {num2} = {result}"
            history.add(calculation_str)

            # Print the result of the calculation
            print(f"Result: {result}")
