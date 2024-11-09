"""
This file contains basic arithmetic functions for addition, subtraction, multiplication,
division, modulus, and exponentiation. Each function takes two float numbers as inputs 
and returns the result of the specified operation. The division and modulus functions 
include error handling to prevent division or modulus by zero.
"""
from app.logging import logger

def addition(a: float, b: float) -> float:
    """This function takes two float numbers as arguments and returns their sum."""
    result = a + b
    logger.info("Performed addition: %s + %s = %s", a, b, result)  # Log addition operation
    return result

def subtraction(a: float, b: float) -> float:
    """Returns the result of subtracting the second number from the first."""
    result = a - b
    logger.info("Performed subtraction: %s - %s = %s", a, b, result)  # Log subtraction operation
    return result

def multiplication(a: float, b: float) -> float:
    """This function takes two float numbers as arguments and returns their product."""
    result = a * b
    logger.info("Performed multiplication: %s * %s = %s", a, b, result)  # Log multiplication operation
    return result

def division(a: float, b: float) -> float:
    """Returns the result of dividing the first number by the second."""
    if b == 0:
        logger.error("Attempted division by zero: %s / %s", a, b)  # Log division by zero error
        raise ValueError("division by zero is not allowed.")
    
    result = a / b
    logger.info("Performed division: %s / %s = %s", a, b, result)  # Log division operation
    return result

def modulus(a: float, b: float) -> float:
    """Returns the remainder when dividing the first number by the second."""
    if b == 0:
        logger.error("Attempted modulus by zero: %s %% %s", a, b)
        raise ValueError("modulus by zero is not allowed.")
    
    result = a % b
    logger.info("Performed modulus: %s %% %s = %s", a, b, result)
    return result

def exponent(a: float, b: float) -> float:
    """Returns the result of raising the first number to the power of the second."""
    result = a ** b
    logger.info("Performed exponentiation: %s ** %s = %s", a, b, result)
    return result
