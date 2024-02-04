def case_counter(text):
    # Initialize counters for uppercase and lowercase letters
    uppercase_count = 0
    lowercase_count = 0

    # Iterate through each character in the string
    for char in text:
        # Check if the character is alphabetic
        if char.isalpha():
            # Check if the character is uppercase
            if char.isupper():
                uppercase_count += 1
            # Check if the character is lowercase
            elif char.islower():
                lowercase_count += 1

    # Print the counts of uppercase and lowercase letters
    print("Uppercase letters:", uppercase_count)
    print("Lowercase letters:", lowercase_count)


