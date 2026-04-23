import csv
# Counter is a built-in tool that counts how many times each item appears in a list
from collections import Counter

# Ask the user to type all the filenames they want to analyze, separated by commas
files = input("Enter the file names(Separate with comma): \n")

# Try to run the code below — if a file isn't found, jump to the except block at the bottom
try:
    # Split the input string into a list of filenames using the comma as a separator
    # e.g. "file1.txt, file2.txt" becomes ["file1.txt", " file2.txt"]
    filename = files.split(",")

    # Remove any extra spaces from each filename so " file2.txt" becomes "file2.txt"
    filename = [f.strip() for f in filename]

    # Create an empty list that will hold every word from every file combined
    all_words = []

    # Loop through each filename in the list one at a time
    for file in filename:

        # Open the current file safely (automatically closes when the block ends)
        with open(file) as f:

            # Print which file we are currently reading
            print(f"For file '{file}': ")

            # Read the entire file content as one long string
            text = f.read()

            # Split the string into a list of individual words
            # e.g. "hello world" becomes ["hello", "world"]
            words = text.split()

            # Add this file's words into the combined all_words list
            all_words.extend(words)

            # Count how many times each word appears in THIS file only
            # e.g. {"the": 5, "hello": 2}
            word_count = Counter(words)

            # Get the 5 most frequent words in this file as a list of (word, count) pairs
            most_common = word_count.most_common(5)

        # Print how many words were in this specific file
        print(f"The total number of words is: {len(words)}")

        # Print a heading before showing the top words for this file
        print("Most common words: \n")

        # Loop through the top 5 words with a 1-based index and print each one
        # each item in most_common is a pair like ("the", 5) which we unpack into word and count
        for i, (word, count) in enumerate(most_common, 1):
            print(f"{i}. {word} - {count} times")

    # Count the total number of words across ALL files combined
    total_words = len(all_words)

    # Count how many times each word appears across ALL files combined
    combined_count = Counter(all_words)

    # Print the total word count across all files
    print(f"Total words across all files: {total_words}")

    # Print a heading for the overall top 10 words
    print("Most common words overall:\n")

    # Loop through the top 10 most common words across all files and print each one
    for i, (word, count) in enumerate(combined_count.most_common(10), 1):
        print(f"{i}. {word} - {count} times")

    # Open (or create) a CSV file called word_count_report.csv for writing
    # newline="" prevents extra blank lines appearing between rows on Windows
    with open("word_count_report.csv", "w", newline="") as csvfile:

        # Create a writer object that knows how to write rows into the CSV file
        writer = csv.writer(csvfile)

        # Write the header row — this becomes the column titles in the CSV
        writer.writerow(["Word", "Count", "Frequency%"])

        # Loop through every word and its count, from most to least common
        for word, count in combined_count.most_common():

            # Calculate what percentage of all words this word makes up
            # e.g. if "the" appears 50 times out of 1000 total, frequency = 5.0%
            frequency = round((count / total_words) * 100, 2)

            # Write one row to the CSV for this word: its name, count, and frequency
            writer.writerow([word, count, f"{frequency}%"])

    # Let the user know the CSV file has been created successfully
    print("Results saved to word_count_report.csv")

# If any of the files weren't found, catch the error and print a helpful message
except FileNotFoundError:
    print(f"File '{files}' Not found")