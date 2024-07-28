import random


# function for choosing random word
def choose_random_word():
    word = ['elephant', 'giraffe', 'lion', 'tiger', 'python', 'programming', 'software', 'development', 'hangman']
    return random.choice(word)


# function for displaying the word
def display_words(word, guessed_words):
    return ''.join(letter if letter in guessed_words else '_ ' for letter in word)


# function for displaying hang man
def display_hangman(incorrect_guesses):
    stages = [
        """
           -----
               |
               |
               |
               |
               |
        =========
        """,
        """
           -----
           |   |
               |
               |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|\  |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|\  |
          /|   |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|\  |
          /|\  |
               |
        =========
        """
    ]
    return stages[incorrect_guesses ]


# main function for hang man game
def hangman():
    word = choose_random_word().lower()  # choosing random word
    guessed_letter = set()  # set of guessed letters
    incorrect_guesses = 0  # set to keep track of guessed letters
    total_incorrect_guesses = 6  # total numer of guesses

    # while loop till correct guess of word or end of total guesses
    while incorrect_guesses < total_incorrect_guesses:
        print(f" \nword : {display_words(word, guessed_letter)}")
        print(f"total guesses you have: {total_incorrect_guesses - incorrect_guesses}")
        print(f"{display_hangman(total_incorrect_guesses - incorrect_guesses )}" )
        guess = input("Guess a letter: ").lower()

        # check if letter is already guessed or not
        if guess in guessed_letter:
            print('Letter already guessed')
            continue

        # checking if guessed letter exists in word or not
        if guess in word:
            guessed_letter.add(guess)  # add guessed letter to the set
            print('You guesed right letter')
        else:
            incorrect_guesses += 1
            print('You guessed Wrong letter ')
        # check if all the letters in the word are guessed or not
        if all(letter in guessed_letter for letter in word):
            print(f"Congratulations! You correctly guessed the word : {word}")
            break
    else:
        print(f"You lost! The correct word was {word}")


if __name__ == '__main__':
    print('Welcome to Hang Man game!!')
    hangman()

