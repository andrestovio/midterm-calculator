def Addition(a: float, b: float) -> float:
    return a + b


def Subtraction(a: float, b: float) -> float:
    return a - b


def Multiplication(a: float, b: float) -> float:
    return a * b  


def Division(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Division by zero is not allowed.")  
    return a / b  