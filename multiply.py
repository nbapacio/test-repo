# This function prompts the user for a number and handles invalid inputs.
def get_number(prompt):
    # Loop indefinitely until a valid number is entered.
    while True:
        try:
            # Attempt to convert user input to a floating-point number.
            value = float(input(prompt))
            # Check for NaN (Not a Number), as it's a valid float but not a desired value.
            # NaN is the only value not equal to itself.
            if value != value:  # Check for NaN
                print("Invalid input: NaN is not allowed")
                continue
            # If input is a valid number, return it and exit the loop.
            return value
        except ValueError:
            # Handle cases where input is not a number (e.g., text).
            print("Invalid input: Please enter a valid number")

# Get the first number from the user.
num1 = get_number("Enter first number: ")
# Get the second number from the user.
num2 = get_number("Enter second number: ")

# Calculate the product of the two numbers.
product = num1 * num2
# Display the final result.
print(f"Product: {product}")
