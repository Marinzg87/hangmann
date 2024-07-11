import random

stages = [
    """
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
""", """
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
""", """
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
""", """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
""", """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
""", """
  +---+
  |   |
  O   |
      |
      |
      |
=========
""", """
  +---+
  |   |
      |
      |
      |
      |
=========
"""]

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

print(f'Pssst, the solution is {chosen_word}.')

display = []
for _ in range(word_length):
    display += "_"
print(display)

end_of_game = False
lives = 6

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = guess
    if guess not in display:
        print(stages[lives])
        lives -= 1

    print(display)

    if "_" not in display:
        end_of_game = True
        print("You win!")

    if lives < 0:
        end_of_game = True
        print("You lose!")