import random

WORDS = ("python", "easy", "great", "friend")
HINTS = ("a snake", "that was so...", "better than good", "companion")

word = random.choice(WORDS)
hint_index = WORDS.index(word)
correct = word
jumble = ''.join(random.sample(word, len(word)))

print("Welcome to WORD JUMBLE!")
print("Unscramble the letters to make a word. GOOD LUCK!\n")
print("The jumble is:", jumble)

attempts = 0
guess = input("\nYour guess: ")

while guess != correct and guess != "":
    print("That's not it! Enter 'hint' to get a hint")
    guess = input("Your guess: ")

    if guess == "hint":
        print("THE HINT:", HINTS[hint_index])
        attempts += 1

if guess == correct:
    print("That's it! You Guessed it.")
    if attempts:
        print("But you needed a tip!")
    else:
        print("Great! You didn't even need a tip!")

input("\nPress Enter to exit")
