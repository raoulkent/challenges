from data import DICTIONARY, LETTER_SCORES, POUCH


NUM_LETTERS = 7


def load_words():
    words = []
    with open(DICTIONARY) as f:
        for line in f:
            words.append(line.strip())
    return words


def calc_word_value(word):
    score = 0
    for letters in word:
        score += LETTER_SCORES.get(letters.upper(), 0)
    return score


def max_word_value(words=None):
    if not words:
        words = load_words()
    scores = map(calc_word_value, words)
    score_list = list(scores)
    max_score = max(score_list)
    max_index = score_list.index(max_score)
    return words[max_index]


def draw_letters():
    draw = []
    with POUCH as p, NUM_LETTERS as nl:
        for card in POUCH:

    return draw


def get_permutations_draw():
    pass


def get_possible_dict_words():
    pass


def validation():
    pass


if __name__ == "__main__":
    """run unittests to validate"""

    # !python3
    # Code Challenge 02 - Word Values Part II - a simple game
    # http://pybit.es/codechallenge02.html
