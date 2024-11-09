"""
This file contains basic arithmetic functions for addition, subtraction, multiplication,
and division. Each function takes two float numbers as inputs and returns the result of 
the specified operation. The division function includes error handling to prevent 
division by zero.
"""
from app.logging import logger

def addition(a: float, b: float) -> float:
    """ Tahis function takes two float numbers as arguments and returns their sum."""
    result = a + b
    logger.info("Performed addition: %s + %s = %s", a, b, result)  # Log addition operation
    return result

def subtraction(a: float, b: float) -> float:
    """ Returns the result of subtracting the second number from the first."""
    result = a - b
    logger.info("Performed subtraction: %s - %s = %s", a, b, result)  # Log subtraction operation
    return result

def multiplication(a: float, b: float) -> float:
    """ This function takes two float numbers as arguments and returns their product."""
    result = a * b
    logger.info("Performed multiplication: %s * %s = %s", a, b, result)  # Log multiplication operation
    return result

def division(a: float, b: float) -> float:
    """ Returns the result of dividing the first number by the second."""
    # It raises a ValueError if the second number (b) is zero to avoid division by zero.
    if b == 0:
        logger.error("Attempted division by zero: %s / %s", a, b)  # Log division by zero error
        raise ValueError("division by zero is not allowed.")
    
    result = a / b
    logger.info("Performed division: %s / %s = %s", a, b, result)  # Log division operation
    return result
