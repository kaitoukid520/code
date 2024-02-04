def fibonacci_sequence(max_value):
    # Handle edge cases for 0 and negative inputs
    if max_value <= 0:
        return "Invalid input. Maximum value must be a positive integer."

    # Initialize the Fibonacci sequence list with the first two values
    sequence = [0, 1]

    # Generate the Fibonacci sequence up to max_value using a while loop
    while sequence[-1] + sequence[-2] <= max_value:
        next_number = sequence[-1] + sequence[-2]
        sequence.append(next_number)

    return sequence

