secretWord = "love"
guessedWord = ""
guess_count = 0
guess_limit = 3

while guessedWord != secretWord and guess_count < guess_limit:
    guessedWord = input('Guess a word: ')
    guess_count += 1


if guess_count == guess_limit and guessedWord != secretWord:
    print('You failed')
else:
    print(f"You succeeded after {guess_count} guesses!")
