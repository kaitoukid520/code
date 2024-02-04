def compound_interest_calculator(P, r, n, t):
    # Validate inputs
    if P <= 0 or r <= 0 or n <= 0 or t <= 0:
        return "Invalid input. All parameters must be positive numbers."

    # Calculate compound interest
    A = P * (1 + r / n) ** (n * t)
    return A

# Test the function
P = float(input("Enter the principal amount (P): "))
r = float(input("Enter the annual interest rate (r) in decimal: "))
n = int(input("Enter the number of times interest is compounded per year (n): "))
t = int(input("Enter the number of years for investment (t): "))

accumulated_amount = compound_interest_calculator(P, r, n, t)
print("Accumulated amount after", t, "years:", accumulated_amount)
