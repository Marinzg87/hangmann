import random
from ascii_art import stages
from words import word_list
from ascii_art import logo

# Randomly choose the word to guess
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

print(logo)
# Little helper to debug code
# print(f'Pssst, the solution is {chosen_word}.')

# Put blanks instead of word characters
display = []
for _ in range(word_length):
    display += "_"

# Game condition and lives counter
end_of_game = False
lives = 6

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    # Info for user that letter has been already guessed
    if guess in display:
        print(f"You've already guessed {guess}.")

    # Replace the blank with correct guess
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = guess

    # Reduce the lives counter by one, if the guess is wrong
    if guess not in display:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        # Check if use still has some lives
        if lives == 0:
            end_of_game = True
            print("You lose!")

    print(f"{' '.join(display)}")

    # Check if user win the game, all blanks are replaced by correct guesses
    if "_" not in display:
        end_of_game = True
        print("You win!")

    # Print the ascii art represented current state of a game
    print(stages[lives])