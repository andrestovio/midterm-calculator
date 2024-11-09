"""
A simple calculator REPL that can perform addition, subtraction, multiplication,
and division. The calculator includes a history feature allowing users to view
past calculations, clear history, undo the last calculation, and automatically
save/load calculation history to/from "default.csv".
"""
from app.logging import logger
# Import the necessary math operations from the operations module
from app.operations import addition, subtraction, multiplication, division

# Import History class from the history module
from app.history import History
import os
from dotenv import load_dotenv

# Load environment
load_dotenv()

def calculator():
    """
    Basic REPL calculator that performs addition, subtraction, multiplication,
    and division, with support for viewing, clearing, undoing, saving, and
    loading calculation history.
    """
    logger.info("Calculator started.")

    print("Welcome to the calculator REPL! Type 'exit' anytime to quit.")
    print("Additional commands: 'history', 'clear', 'undo', 'save', 'load'.")

    history = History()

    while True:
        user_input = input(
            "Enter an operation (add, subtract, multiply, divide) and two "
            "numbers, or a command (history, clear, undo, save, load): "
        )
        logger.info("User input received: %s", user_input)

        if user_input.lower() == "exit":
            logger.info("Calculator exited by user.")
            print("Exiting calculator...")
            break

        elif user_input.lower() == "history":
            logger.info("Displaying calculation history.")
            print("Calculation History:")
            for calc in history.get_history():
                print(calc)
            continue

        elif user_input.lower() == "clear":
            history.clear()
            logger.info("Calculation history cleared.")
            print("History cleared.")
            continue

        elif user_input.lower() == "undo":
            history.undo_last()
            logger.info("Last calculation undone.")
            print("Last calculation undone.")
            continue

        elif user_input.lower() == "save":
            history_file = os.getenv("HISTORYCSV_FILE", "default.csv")
            history.save(history_file)
            logger.info("Calculation history saved to %s.", history_file)
            print(f"History saved to {history_file}.")
            continue

        elif user_input.lower() == "load":
            history_file = os.getenv("HISTORYCSV_FILE", "default.csv")
            history.load(history_file)
            logger.info("Calculation history loaded from %s.", history_file)
            print(f"History loaded from {history_file}.")
            continue

        else:
            try:
                operation, num1, num2 = user_input.lower().split()
                num1, num2 = float(num1), float(num2)
                logger.info("Operation: %s, Num1: %s, Num2: %s", operation, num1, num2)
            except ValueError:
                logger.error("Invalid input format for operation.")
                print("Invalid input. Please follow the format: <operation> <num1> <num2>")
                continue

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
                    logger.error("Division by zero attempted.")
                    print(error)
                    continue
            else:
                logger.warning("Unknown operation: %s", operation)
                print(f"Unknown operation '{operation}'. Supported operations: add, subtract, multiply, divide.")
                continue

            calculation_str = f"{operation} {num1} {num2} = {result}"
            history.add(calculation_str)
            logger.info("Performed calculation: %s", calculation_str)

            print(f"Result: {result}")
