import sys  # Import the sys module

# Print the current Python version
print("Python version:", sys.version)

# Check if enough arguments were passed (script name + 3 more)
if len(sys.argv) < 4:
    print("Usage: python calculator.py <num1> <operation> <num2>")
    print("Example: python calculator.py 10 add 5")
    sys.exit()  # Exit the program early if not enough input

# Get values from command-line arguments
num1 = float(sys.argv[1])      # First number
operation = sys.argv[2]        # Operation (add, sub, mul, div)
num2 = float(sys.argv[3])      # Second number

# Perform the operation
if operation == "add":
    result = num1 + num2
elif operation == "sub":
    result = num1 - num2
elif operation == "mul":
    result = num1 * num2
elif operation == "div":
    if num2 == 0:
        print("Cannot divide by zero")
        sys.exit()
    result = num1 / num2
else:
    print("Invalid operation. Use: add, sub, mul, div")
    sys.exit()

# Show the result
print(f"Result of {num1} {operation} {num2} = {result}")

# Show memory used by result
print("Memory used by result:", sys.getsizeof(result), "bytes")

# Print paths where Python looks for modules
print("\nPython searches for modules in:")
for path in sys.path:
    print(path)

# Print the first 5 loaded module names
print("\nFirst 5 loaded modules:")
print(list(sys.modules.keys())[:5])

