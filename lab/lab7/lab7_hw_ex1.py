import argparse

def main():
    parser = argparse.ArgumentParser(description="Compute basic operations on two numbers.")
    
    # Adding positional arguments for two numbers
    parser.add_argument("num1", type=float, help="First number")
    parser.add_argument("num2", type=float, help="Second number")
    
    args = parser.parse_args()
    
    # Retrieving arguments
    num1 = args.num1
    num2 = args.num2
    
    # Calculating results
    addition = num1 + num2
    subtraction = num1 - num2
    multiplication = num1 * num2
    division = num1 / num2 if num2 != 0 else "undefined (division by zero)"
    mean = (num1 + num2) / 2
    
    # Printing results
    print(f"Sum: {addition}")
    print(f"Difference: {subtraction}")
    print(f"Multiplication: {multiplication}")
    print(f"Division: {division}")
    print(f"Mean: {mean}")

if __name__ == "__main__":
    main()

