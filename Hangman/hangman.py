from words import words_list
import random
import string


def get_valid_word(words_list):
    word = random.choice(words_list)  # randomly chooses from that word list
    while "-" in word or " " in word:
        word = random.choice(words_list)

    return word.upper()


def hangman():
    word = get_valid_word(words_list)
    word_letters = set(word)  #  letters in the word.
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # what the user has guessed

    lives = 7

    # getting user input
    while len(word_letters) > 0 and lives > 0:
        #  Letters used
        # ' '.join(['a','b','c','d']) ='a b c d'
        print(f"You have {lives} lives left and you have used these letter: ", ' '.join(used_letters))

        # what current word is(ie w - R D)
        disp_word_list = [letter if letter in used_letters else '-' for letter in word]
        print("Current word is: ", ' '.join(disp_word_list))

        user_letter = input(" Guess a letter : ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives -1  # takes away a life if wrong
                print(f"\n Your letter {user_letter} is not in the word.")

        elif user_letter in used_letters:
            print("You have already used that character, please try again.")      

        else:
            print("Invalid character,pls try again")

    # gets here when len(words_letters) is 0
    if lives == 0:
        print("You died sorry,The word was ", word)
    else:
        print(f"Yay! You guessed the word {word} !!!")


if __name__ == '__main__':
    hangman()