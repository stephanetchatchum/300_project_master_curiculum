import random

words = [
    "python", "hangman", "programming", "computer", "algorithm", 
    "function", "variable", "keyboard", "monitor", "network",
    "database", "software", "hardware", "internet", "password",
    "encryption", "server", "client", "protocol", "framework"
]
def get_random_word(word_list):
    # pick and return a random word
    word = random.choice(words)
    return word

def draw_hangman(wrong_guesses):
    
    stages = [
        # stage 0 - no wrong guesses
        """
            +----+
            |    |
                 |
                 |
                 |
                 |
        ==========
        """,
        # stage 1 - head
        """
            +----+
            |    |
            O    |
                 |
                 |
                 |
        ==========
        """,
        """
            +----+
            |    |
            O    |
            |    |
                 |
                 |
        ==========
        """,
        """
            +----+
            |    |
            O    |
           /|    |
                 |
                 |
        ==========
        """,
        """
            +----+
            |    |
            O    |
           /|\   |
                 |
                 |
        ==========
        """,
        """
            +----+
            |    |
            O    |
           /|\   |
           /     |
                 |
        ==========
        """,
        """
            +----+
            |    |
            O    |
           /|\   |
           / \   |
                 |
        ==========
        """
    ]
    print(stages[wrong_guesses])

def display_state(word, guessed_letters, wrong_guesses):
    # show word with blanks, guessed letters, attempts left
    word_display = " ".join(letter if letter in guessed_letters else "_" for letter in word)

    if guessed_letters:
        guessed_display = ", ".join(sorted(guessed_letters))
    else:
        guessed_display = "none"

    print(f"\nWord: {word_display}")
    print(f"Guessed: {guessed_display}")
    print(f"Attempts left: {6 - wrong_guesses}")


def get_guess(guessed_letters):
    # get a valid single letter that hasn't been guessed yet
    while True:
        letter = input("Enter your guess:\n").lower()
        if letter == "" or not letter.isalpha():
            print("Invalid, enter a letter")
            continue
        if letter in guessed_letters:
            print("WARNING, you already guessed this")
            continue
        return letter

    
def is_word_complete(word, guessed_letters):
    # return True if all letters in word have been guessed
    return all(letter in guessed_letters for letter in word)

def play_game():
    word = get_random_word(words)
    guessed_letters = set()
    wrong_guesses = 0
    while wrong_guesses < 6 and not is_word_complete(word, guessed_letters):
        draw_hangman(wrong_guesses)
        display_state(word, guessed_letters, wrong_guesses)
        g_letter = get_guess(guessed_letters)
        guessed_letters.add(g_letter)
        if g_letter not in word:
            wrong_guesses += 1
        else:
            print("Correct")
    draw_hangman(wrong_guesses)
    if is_word_complete(word, guessed_letters):
        print("You win")
    else:
        print(f"You lose! The word was: {word}")

def main():
    play_game()

if __name__ == "__main__":
    main()