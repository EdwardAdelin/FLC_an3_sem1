import argparse

def main():
    parser = argparse.ArgumentParser(description="Perform an operation on two numbers based on a given symbol.")
    
    # Adding positional arguments for two numbers
    parser.add_argument("num1", type=float, help="First number")
    parser.add_argument("num2", type=float, help="Second number")
    parser.add_argument("operation", type=str, choices=["+", "-", "*", "/", "mean"],
                        help="Operation to perform: +, -, *, /, or mean")

    args = parser.parse_args()
    
    # Retrieve arguments
    num1 = args.num1
    num2 = args.num2
    operation = args.operation
    
    # Perform the operation based on the symbol
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        result = num1 / num2 if num2 != 0 else "undefined (division by zero)"
    elif operation == "mean":
        result = (num1 + num2) / 2

    # Display the result
    print(f"Result: {result}")

if __name__ == "__main__":
    main()
