def morse_translator(text):
    # Morse code mapping
    morse_code_dict = {
        "A": ".-",
        "B": "-...",
        "C": "-.-.",
        "D": "-..",
        "E": ".",
        "F": "..-.",
        "G": "--.",
        "H": "....",
        "I": "..",
        "J": ".---",
        "K": "-.-",
        "L": ".-..",
        "M": "--",
        "N": "-.",
        "O": "---",
        "P": ".--.",
        "Q": "--.-",
        "R": ".-.",
        "S": "...",
        "T": "-",
        "U": "..-",
        "V": "...-",
        "W": ".--",
        "X": "-..-",
        "Y": "-.--",
        "Z": "--..",
    }

    # Convert the input text to uppercase
    text = text.upper()
    morse_code = []

    # Iterate through each word in the text
    for word in text.split():
        word_morse_code = []
        # Iterate through each character in the word
        for char in word:
            # Check if the character is alphabetic

            if char.isalpha():
                # Get the Morse code for the character and append it to the word_morse_code list
                word_morse_code.append(morse_code_dict[char])
        # Join the Morse code for characters using space and append it to the morse_code list
        morse_code.append(" ".join(word_morse_code))

    # Join the Morse code for words using slash and return the result
    return " / ".join(morse_code)


# Test the function
text = input("Enter text to translate into Morse code: ")
print("Morse code:", morse_translator(text))
