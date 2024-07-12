import random
from ascii_art import stages
from words import word_list
from ascii_art import logo

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

print(logo)
print(f'Pssst, the solution is {chosen_word}.')

display = []
for _ in range(word_length):
    display += "_"
# print(display)

end_of_game = False
lives = 6

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed {guess}.")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = guess

    if guess not in display:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        if lives == 0:
            end_of_game = True
            print("You lose!")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win!")

    print(stages[lives])