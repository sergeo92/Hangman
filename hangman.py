import random


def game():
    list_ = ["java", "javascript", "kotlin", "python"]
    word_random = random.choice(list_)
    list_word_random = list(word_random)
    word_guess = ['-'] * len(word_random)
    i = 0
    type_letter = ""

    while i != 8:
        print()
        print("".join(word_guess))
        letter = input("enter a letter: ")

        if len(letter) != 1:
            print("You should input a single letter")

        elif letter.isupper() or letter.isnumeric() or letter.isalpha() == False:
            print("It is not an ASCII lowercase letter")

        else:

            if letter in word_guess or letter in type_letter:
                print("You already typed this letter")
                continue

            elif letter not in word_random:
                print("No such letter in the word")
                i += 1

            elif "".join(word_guess) == word_random:
                i += 1

            else:

                for elt in list_word_random:

                    if elt == letter:
                        indice = list_word_random.index(elt)
                        word_guess[indice] = elt
                        list_word_random[indice] = '-'
            type_letter += letter

    if word_random == "".join(word_guess):
        print(f"{word_random}\nYou guessed the word!\nYou survived!")
        print()
    else:
        print("You are hanged!")
        print()


print("H A N G M A N")
while True:

    start_game = input("Type play to play the game, exit to quit: ")

    if start_game == "exit":
        break
    else:
        game()
        break
