import random

print("HANGMAN")
words = ["python", "java", "javascript", "php"]

while True:
    menu = input('Type "play" to play the game, "exit" to quit: ')

    if menu == "exit":
        break
    elif menu == "play":
        secret_word = random.choice(words)
        hidden_word = list("-" * len(secret_word))
        attempts = 8
        guessed_letters = []

        while attempts > 0:
            print()
            print("".join(hidden_word))

            if "-" not in hidden_word:
                print(f"You guessed the word {secret_word}!")
                print("You survived!")
                break

            guess = input("Input a letter: ")

            if len(guess) != 1:
                print("You should input a single letter")
                continue

            if not guess.islower() or not guess.isalpha() or not guess.isascii():
                print("Please enter a lowercase English letter")
                continue

            if guess in guessed_letters:
                print("You've already guessed this letter")
                continue

            guessed_letters.append(guess)

            if guess in secret_word:
                for i in range(len(secret_word)):
                    if secret_word[i] == guess:
                        hidden_word[i] = guess
            else:
                print("That letter doesn't appear in the word")
                attempts -= 1

        if attempts == 0 and "-" in hidden_word:
            print("You lost!")

    else:
        continue

