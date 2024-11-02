from app.operations import addition, subtraction, multiplication, division


def calculator():
    print("Welcome to the calculator REPL! Type 'exit' anytime to quit.")


    while True:
        user_input = input("Enter an operation (add, subtract, multiply, divide) and two numbers: ")


        # Handle the 'exit' command.
        if user_input.lower() == "exit":
            print("Exiting calculator...")
            break


        # Process the input as a calculation.
        else:
            try:
                # Try to split the input into operation and numbers.
                operation, num1, num2 = user_input.lower().split()
                num1, num2 = float(num1), float(num2)
            except ValueError:
                print("Invalid input. Please follow the format: <operation> <num1> <num2>")
                continue


            # Perform the requested operation.
            if operation == "add":
                result = addition(num1, num2)
            elif operation == "subtract":
                result = subtraction(num1, num2)
            elif operation == "multiply":
                result = multiplication(num1, num2)
            elif operation == "divide":
                try:
                    result = division(num1, num2)
                except ValueError as e:
                    print(e)
                    continue
            else:
                print(f"Unknown operation '{operation}'. Supported operations: add, subtract, multiply, divide.")
                continue


            # Print the result.
            print(f"Result: {result}")
