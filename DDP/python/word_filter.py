def word_filter_counter(text, filter_words):
    # Convert all words in filter_words to lowercase for case-insensitive comparison
    filter_words_lower = [word.lower() for word in filter_words]

    # Initialize a dictionary to store filtered words and their counts
    filtered_word_counts = {}

    # Split the text into words
    words = text.split()

    # Iterate through each word in the text
    for word in words:
        # Remove punctuation marks from the word
        word = ''.join(char for char in word if char.isalnum())

        # Convert the word to lowercase for case-insensitive comparison
        word_lower = word.lower()

        # Check if the lowercase word is in the filter_words_lower list
        if word_lower in filter_words_lower:
            # Increment the count of the filtered word in the dictionary
            filtered_word_counts[word_lower] = filtered_word_counts.get(word_lower, 0) + 1

    return filtered_word_counts
