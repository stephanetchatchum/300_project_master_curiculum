# Counter is a built-in tool that counts how many times each item appears in a list
from collections import Counter

# Ask the user to enter the name (or path) of the file they want to analyze
filename = input("Enter the file name: \n")

# Try to open and process the file — if it doesn't exist, jump to the except block
try:

    # Open the file (automatically closes it when the block is done)
    with open(filename) as f:

        # Read the entire file content as one big string
        text = f.read()

        # Split the string into a list of individual words (splits on spaces/newlines)
        words = text.split()

        # Count how many times each word appears e.g. {"the": 5, "hello": 2, ...}
        word_count = Counter(words)

        # Get the 5 most frequently occurring words as a list of (word, count) pairs
        most_common = word_count.most_common(5)

    # Print the total number of words
    print(f"The total number of words is: {len(words)}")

    # Print a heading before listing the results
    print("Most common words: \n")

    # Loop through the top 5 words with a 1-based index
    # Each item in most_common is a pair like ("the", 5), so we unpack into (word, count)
    for i, (word, count) in enumerate(most_common, 1):
        print(f"{i}. {word} - {count} times")

# If the file doesn't exist, catch the error and print a friendly message
except FileNotFoundError:
    print(f"File '{filename}' Not found")