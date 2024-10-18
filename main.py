# Importing the "calculator" function from the "calculator.py" file located in the "app" folder.
# This allows us to use the calculator functionality in our program.
from app.calculator import calculator

# This block checks if the current file is being executed directly, rather than being imported by another file.
# If it's being run directly, Python assigns the value "__main__" to the special variable "__name__".
# This ensures that the following code will only execute when the file is run as a script.
if __name__ == "__main__":

    calculator()
