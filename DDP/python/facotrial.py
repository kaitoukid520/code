def calculate_factorial(number):
    # Handle edge cases for 0 and negative inputs
    if number < 0:
        return "Factorial is not defined for negative numbers."
    elif number == 0:
        return 1

    # Initialize the factorial to 1
    factorial = 1

    # Calculate factorial using a for loop
    for i in range(1, number + 1):
        factorial *= i

    return factorial
