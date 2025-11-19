def get_number(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value != value:  # Check for NaN
                print("Invalid input: NaN is not allowed")
                continue
            return value
        except ValueError:
            print("Invalid input: Please enter a valid number")

num1 = get_number("Enter first number: ")
num2 = get_number("Enter second number: ")
product = num1 * num2
print(f"Product: {product}")
