import random

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

print(f'Pssst, the solution is {chosen_word}.')

display = []
for _ in range(word_length):
    display += "-"
print(display)

counter = word_length
print(f"Counter on the beginning: {counter}")
while counter > 0:
    guess = input("Guess a letter: ").lower()

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = guess
            counter -= 1

    print(display)
print("You win!")