import random

secret_words = ["apple", "banana", "mango", "strawberry",
                "orange", "grape", "pineapple", "apricot",
                "lemon", "coconut", "watermelon", "cherry",
                "papaya", "berry", "peach", "lychee", "muskmelon"]

letter_guessed = ""
turn = 14


def split(word):
    return [char for char in word]


if __name__ == "__main__":
    random_fruit = random.choice(secret_words)
    split_random_fruit = split(random_fruit)

    print("Guess the word! HINT: word is a name of a fruit")

    for letter in random_fruit:
        print("_", end=" ")

    print("\n")

    word_length = len(random_fruit)

    while turn > 0:
        guess = input("Guess a letter: ")
        letter_guessed += guess

        if guess == "":
            print("ENTER A LETTER")
        if guess != "":
            for char in random_fruit:
                if char in letter_guessed:
                    print(char)
                else:
                    print("_")

            if guess in random_fruit:
                print("Correct")
            else:
                print("Wrong")
                turn -= 1

        print(f"All guesses: {letter_guessed}")
    print(f"The word was: {random_fruit}")
