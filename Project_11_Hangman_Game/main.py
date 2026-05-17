import random  # import random module to pick a random word from the list

# List of words the game will randomly pick from
# At least 20 words covering programming and tech vocabulary
words = [
    "python", "hangman", "programming", "computer", "algorithm", 
    "function", "variable", "keyboard", "monitor", "network",
    "database", "software", "hardware", "internet", "password",
    "encryption", "server", "client", "protocol", "framework"
]

def get_random_word(word_list):
    # Pick and return one random word from the word list
    # random.choice() selects a random item from any sequence
    word = random.choice(word_list)
    return word

def draw_hangman(wrong_guesses):
    # List of 7 ASCII art stages — one per wrong guess (0 to 6)
    # Each stage is a multi-line string using triple quotes
    # We index into this list using wrong_guesses e.g. stages[3] = 3 wrong guesses
    stages = [
        # stage 0 - no wrong guesses yet, empty gallows
        """
            +----+
            |    |
                 |
                 |
                 |
                 |
        ==========""",
        # stage 1 - head appears
        """
            +----+
            |    |
            O    |
                 |
                 |
                 |
        ==========""",
        # stage 2 - body appears
        """
            +----+
            |    |
            O    |
            |    |
                 |
                 |
        ==========""",
        # stage 3 - left arm appears
        """
            +----+
            |    |
            O    |
           /|    |
                 |
                 |
        ==========""",
        # stage 4 - right arm appears
        """
            +----+
            |    |
            O    |
           /|\   |
                 |
                 |
        ==========""",
        # stage 5 - left leg appears
        """
            +----+
            |    |
            O    |
           /|\   |
           /     |
                 |
        ==========""",
        # stage 6 - right leg appears, full hangman, game over
        """
            +----+
            |    |
            O    |
           /|\   |
           / \   |
                 |
        =========="""
    ]

    # Print the stage that matches the current number of wrong guesses
    print(stages[wrong_guesses])

def display_state(word, guessed_letters, wrong_guesses):
    # Build the word display — show the letter if it has been guessed, otherwise show _
    # This is a generator expression inside join() — loops through each letter in the word
    # e.g. for "python" with guessed p and t: "p _ t _ _ _"
    word_display = " ".join(letter if letter in guessed_letters else "_" for letter in word)

    # Build the guessed letters display
    # sorted() puts the letters in alphabetical order for readability
    # join() puts commas between them e.g. "a, e, p, t"
    if guessed_letters:
        guessed_display = ", ".join(sorted(guessed_letters))
    else:
        guessed_display = "none"  # shown at the start before any guesses

    # Print the current game state
    print(f"\nWord: {word_display}")
    print(f"Guessed: {guessed_display}")
    print(f"Attempts left: {6 - wrong_guesses}")  # 6 total minus how many wrong so far

def get_guess(guessed_letters):
    # Keep asking until the player gives a valid new letter
    while True:
        # Get input and convert to lowercase so "A" and "a" are treated the same
        letter = input("Enter your guess:\n").lower()

        # Reject empty input or anything that isn't a letter (digits, symbols etc.)
        # isalpha() returns True only if the string contains only letters
        if letter == "" or not letter.isalpha():
            print("Invalid, enter a letter")
            continue  # go back to the top of the loop and ask again

        # Reject input longer than one character
        if len(letter) > 1:
            print("Enter a single letter only")
            continue

        # Warn if the letter was already guessed — don't penalize, just ask again
        # guessed_letters is a set so checking membership is very fast
        if letter in guessed_letters:
            print("WARNING, you already guessed this")
            continue

        # All checks passed — return the valid letter
        return letter

def is_word_complete(word, guessed_letters):
    # Return True if every letter in the word has been guessed
    # all() returns True only if the condition is True for every item
    # e.g. for "cat" — checks if 'c' in guessed, 'a' in guessed, 't' in guessed
    return all(letter in guessed_letters for letter in word)

def play_game():
    # Pick a random word from the words list to start the game
    word = get_random_word(words)

    # Use a set for guessed letters — sets automatically prevent duplicates
    # and checking membership with 'in' is faster than a list
    guessed_letters = set()

    # Track how many wrong guesses have been made — starts at 0
    wrong_guesses = 0

    # Keep playing as long as the player hasn't used all 6 guesses
    # AND the word hasn't been fully guessed yet
    while wrong_guesses < 6 and not is_word_complete(word, guessed_letters):

        # Show the current hangman drawing for this stage
        draw_hangman(wrong_guesses)

        # Show the word with blanks, guessed letters and attempts remaining
        display_state(word, guessed_letters, wrong_guesses)

        # Get a valid letter from the player
        g_letter = get_guess(guessed_letters)

        # Add the guessed letter to the set of guessed letters
        guessed_letters.add(g_letter)

        # Check if the guess was correct
        if g_letter not in word:
            # Wrong guess — increment the wrong guess counter
            wrong_guesses += 1
            print(f"Wrong! '{g_letter}' is not in the word.")
        else:
            print(f"Correct! '{g_letter}' is in the word.")

    # Draw the final hangman state after the game ends
    draw_hangman(wrong_guesses)

    # Check the outcome — did the player win or lose?
    if is_word_complete(word, guessed_letters):
        # All letters guessed before running out of attempts
        print("🎉 You win! Well done!")
    else:
        # Ran out of attempts — reveal the word
        print(f"💀 You lose! The word was: {word}")

def main():
    # Entry point — just starts the game
    play_game()

# Only run main() if this file is run directly, not imported
if __name__ == "__main__":
    main()