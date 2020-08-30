# test_hangman.py

import hangman


# A. Getting secret word
# 1. Secret word should have atleast 6 letters
# 2. Secret word should have no punctuation
# 3. Secret word should not be a proper noun

def test_secret_word_6_letters():
    assert all(hangman.get_secret_word("./test_data/1.words") == "policeman" for _ in range(100))


def test_secret_word_no_punctuation():
    assert all(hangman.get_secret_word("./test_data/2.words") == "fireman" for _ in range(100))


def test_secret_word_no_proper_nouns():
    assert all(hangman.get_secret_word("./test_data/3.words") == "policeman" for _ in range(100))


# B. Masking secret word    
# 1. Masks entire word when not guessed.
# 2. Unmasks entire word when fully guessed.
# 3. Unmasks for words with repetitive letters.
#    Do not masks for wrong guesses.

def test_mask_word():
    word = "gangman"
    guess = ""
    assert hangman.mask_word(word, guess) == "*******"


def test_mask_word_guessed():
    words = ["python", "tigers", "whales"]
    assert all([hangman.mask_word(i, i) == i for i in words])


def test_mask_word_repetitive():
    words = ["deadpool", "batman", "greenlantern"]
    guess = ["kvwvkod", "qwewqa", "zxyxzen"]
    masks = ["d**d*oo*", "*a**a*", "**een**n*e*n"]
    assert all([hangman.mask_word(words[i], guess[i]) == masks[i] for i in range(len(words))])


# C. Checking inputs
# 1. Condition1:  One letter guesses
# 2. Condition2:  No repetitive guesses
# 3. Condition3:  Only alphabets
# 4. Changes uppercase to lowercase

def test_check_cond1():
    guess = ["you", "we", "u", "i", "v"]
    result = [("Only a single letter is allowed", False), ("Only a single letter is allowed", False), ("", True),
              ("", True), ("", True)]
    assert all([hangman.check_cond1(guess[i]) == result[i] for i in range(len(guess))])


def test_check_cond2():
    guess_f = ["a", "b", "c"]
    guess_t = ["d", "e", "f"]
    guess_list = "qawbrc"
    assert all([hangman.check_cond2(guess_t[i], guess_list) == ("", True) for i in range(len(guess_t))])
    assert all(
        [hangman.check_cond2(guess_f[i], guess_list) == ("Already guessed '{}'".format(guess_f[i]), False) for i in
         range(len(guess_f))])


def test_check_cond3():
    guess = ["1", "?", "n", "o", "f"]
    result = [("Only alphabets are allowed", False), ("Only alphabets are allowed", False), ("", True), ("", True),
              ("", True)]
    assert all([hangman.check_cond3(guess[i]) == result[i] for i in range(len(guess))])


def test_upper_to_lower():
    guess = ["A", "B", "C", "d", "e", "f"]
    result = ["a", "b", "c", "d", "e", "f"]
    assert all([hangman.upper_to_lower(guess[i]) == result[i] for i in range(len(guess))])


def test_guess_evaluator():
    guess = ["A", "e", "f"]
    guess_list = "zxy"
    result = [("", True), ("", True), ("", True)]
    assert all([hangman.guess_evaluator(guess[i], guess_list) == result[i] for i in range(len(guess))])


def test_guess_evaluator_cond1():
    guess1 = ["wou", "sss", "123", "zy"]
    guess_list = "zxy"
    result = ("Only a single letter is allowed", False)
    assert all([hangman.guess_evaluator(guess1[i], guess_list) == result for i in range(len(guess1))])


def test_guess_evaluator_cond2():
    guess2 = ["x", "z", "y"]
    guess_list = "xzy"
    assert all(
        [hangman.guess_evaluator(guess2[i], guess_list) == ("Already guessed '{}'".format(guess2[i]), False) for i in
         range(len(guess2))])


def test_guess_evaluator_cond3():
    guess3 = ["?", "1", "#"]
    guess_list = "zxy"
    result = ("Only alphabets are allowed", False)
    assert all([hangman.guess_evaluator(guess3[i], guess_list) == result for i in range(len(guess3))])


# E. Counting wrong guesses
def test_wrong_guesses():
    words = ["python", "tigers", "whales", "elephant"]
    guesslist = ["lthwea", "qwerty", "asdfe", "qwdtfe"]
    result = [4, 3, 2, 4]
    assert all([hangman.wrong_guesses(words[i], guesslist[i]) == result[i] for i in range(len(words))])
