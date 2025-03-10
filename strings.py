"""Functions for creating, transforming, and adding prefixes to strings."""


def add_prefix_un(word):
    newWord = "un" + word
    return newWord


def make_word_groups(vocab_words):
    prefix = vocab_words[0]
    newWords = f" :: {prefix}".join(vocab_words)
    return newWords


def remove_suffix_ness(word):
    rootWord = word[:-4];
    print(rootWord)
    if rootWord.endswith("i"):
        correctedRootWord = rootWord[-1] + "y"
        print(correctedRootWord)
        return correctedRootWord
    else:
        return rootWord

def adjective_to_verb(sentence, index):
    """Change the adjective within the sentence to a verb.

    :param sentence: str - that uses the word in sentence.
    :param index: int - index of the word to remove and transform.
    :return: str - word that changes the extracted adjective to a verb.

    For example, ("It got dark as the sun set.", 2) becomes "darken".
    """

    pass
