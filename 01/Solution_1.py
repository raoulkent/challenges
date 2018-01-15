from data import DICTIONARY, LETTER_SCORES


def load_words():
    """Load dictionary into a list and return list"""

    words = []
    with open(DICTIONARY) as f:
        for line in f:
            words.append(line.strip())
    return words


def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""

    score = 0
    for letters in word:
        score += LETTER_SCORES.get(letters.upper(), 0)
    return score


def max_word_value(words=None):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""

    if not words:
        words = load_words()
    scores = map(calc_word_value, words)
    scorelist = list(scores)
    maxscore = max(scorelist)
    maxindex = scorelist.index(maxscore)
    return words[maxindex]


if __name__ == "__main__":
    # run unittests to validate
    load_words()
