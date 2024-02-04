def is_leap_year(year):
    # Check if the year is divisible by 4
    if year % 4 == 0:
        # If the year is divisible by 100, it's a century year
        if year % 100 == 0:
            # If the year is divisible by 400, it's a leap year
            if year % 400 == 0:
                return True
            else:
                return False
        # If the year is not divisible by 100, it's a leap year
        else:
            return True
    # If the year is not divisible by 4, it's not a leap year
    else:
        return False


