import random
import time


def mask_word(s_word, guessed):
    "masks letters in 's_word' unless they are in 'guessed'"
    mask = []
    for i in s_word:
        if i in guessed:
            mask.append(i)
        else:
            mask.append("*")
    return "".join(mask)


def check_cond(guessed):
    "checks input-condition 1: One letter guesses"
    if len(guessed) == 1:
        return "", True
    return "Only a single letter is allowed", False


def upper_to_lower(guess):
    "input-condition 4: changes uppercase to lowercase"
    if guess.isupper():
        return guess.lower()
    return guess


def guess_evaluator(guessed, guess_list):
    "guess_evaluator: checks all the input-conditions"
    guessed = upper_to_lower(guessed)

    if not check_cond(guessed)[1]:
        return check_cond(guessed)

    return "", True


def guess_manager(guessed, guess_list):
    """guess_manager: prints string for failed input-condition
and asks for new input"""
    while not guess_evaluator(guessed, guess_list)[1]:
        print(guess_evaluator(guessed, guess_list)[0])
        guessed = input("Enter another guess: ")
    return guessed


def wrong_guesses(s_word, guess_list):
    "wrong_guess: returns the number of wrong guesses"
    count = 0
    for i in guess_list:
        if i not in s_word:
            count += 1
    return count


def main():
    with open("./test_data/words") as words:
        good_words = []
        for i in words:
            i = i.strip()
            if len(i) <= 6:  # No short words
                continue
            if not i.isalpha():  # No punctuation
                continue
            if i[0].isupper():  # No proper nouns
                continue
            good_words.append(i)
    secret_word = random.choice(good_words)
    print("""
    Welcome to hangman!
    You have to guess the secret-word before 6 wrong tries.
    Secret-word have {} letters
    .
    """.format(len(secret_word)))
    formatter = "\nWord: {:^15}    Life:{:<12}   Guessed: {:<10}"
    guesslist = ""
    game_won = "no"

    # Game losses when 6 guesses are wrong
    while not wrong_guesses(secret_word, guesslist) == 6:
        newguess = input("Enter a guess: ")
        newguess = guess_manager(newguess, guesslist)  # Checking conditions

        guesslist += newguess  # guesslist updates
        guesslist = "".join(sorted(set(guesslist)))  # sorting guesslist

        life = (len(secret_word) - wrong_guesses(secret_word, guesslist))
        print(formatter.format(mask_word(secret_word, guesslist), life, guesslist))

        if secret_word == mask_word(secret_word, guesslist):
            print("\n\nCongratulations!")
            game_won = "yes"
            break

    if game_won == "no":
        time.sleep(0.5)
        print("\nToo bad! The secret word was '{}'".format(secret_word))


# import-guard
if __name__ == '__main__':
    main()