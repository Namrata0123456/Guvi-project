import random

# List of words
words = ['python', 'javascript', 'java', 'automation', 'pytest', 'guvi', 'selenium']

def scramble_word(word):
    return ''.join(random.sample(word, len(word)))

def play_game():
    word = random.choice(words)
    scrambled = scramble_word(word)
    print(f"Unscramble this word: {scrambled}")

    attempts = 3
    while attempts > 0:
        guess = input("Your guess: ").lower()
        if guess == word:
            print("Correct! Well done.")
            break
        else:
            attempts -= 1
            print(f"Wrong guess! {attempts} attempts left.")
    else:
        print(f"Out of attempts! The word was: {word}")

play_game()