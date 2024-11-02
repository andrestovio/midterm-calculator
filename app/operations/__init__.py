"""
This file contains basic arithmetic functions for Addition, Subtraction, Multiplication,
and Division. Each function takes two float numbers as inputs and returns the result of 
the specified operation. The Division function includes error handling to prevent 
Division by zero.
"""

def addition(a: float, b: float) -> float:
    """ This function takes two float numbers as arguments and returns their sum."""
    return a + b

def subtraction(a: float, b: float) -> float:
    """ Returns the result of subtracting the second number from the first."""
    return a - b

def multiplication(a: float, b: float) -> float:
    """ This function takes two float numbers as arguments and returns their product."""
    return a * b

def division(a: float, b: float) -> float:
    """ Returns the result of dividing the first number by the second."""
    # It raises a ValueError if the second number (b) is zero to avoid division by zero.
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    return a / b
