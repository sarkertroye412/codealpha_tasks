import random

words = ["python", "coding", "laptop", "planet", "guitar"] # 5 predefined words
word = random.choice(words)

guessed = []      
wrong = 0         
max_wrong = 6     

print("=== HANGMAN ===")
print("Guess the word one letter at a time.")
print("You can make only", max_wrong, "wrong guesses.\n")

while wrong < max_wrong:
    display = ""
    for letter in word:
        if letter in guessed:
            display += letter + " "
        else:
            display += "_ "
    print("Word:", display)

    if "_" not in display:
        print("\nCongratulations! You guessed the word:", word)
        break

    print("Wrong guesses left:", max_wrong - wrong)
    print("Guessed letters:", " ".join(guessed))

    # get input from player
    guess = input("Enter a letter: ").lower()

    # check the input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.\n")
        continue

    if guess in guessed:
        print("You already guessed that letter.\n")
        continue

    guessed.append(guess)

    if guess in word:
        print("Good guess!\n")
    else:
        wrong += 1
        print("Wrong guess!\n")


if wrong == max_wrong:
    print("Game over! The word was:", word)