def is_prime(number):
    # Check if the number is less than 2
    if number < 2:
        return False
    
    # Iterate from 2 to the square root of the number
    # If the number is divisible by any integer in this range, it's not a prime number
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    
    # If the loop completes without finding a divisor, the number is prime
    return True

