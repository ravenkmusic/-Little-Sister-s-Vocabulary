"""Functions for creating, transforming, and adding prefixes to strings."""
import string

def add_prefix_un(word):
    newWord = "un" + word
    return newWord


def make_word_groups(vocab_words):
    prefix = vocab_words[0]
    newWords = f" :: {prefix}".join(vocab_words)
    return newWords


def remove_suffix_ness(word):
    rootWord = word[:-4];
    if rootWord.endswith("i"):
        correctedRootWord = rootWord[:-1] + "y"
        print(correctedRootWord)
        return correctedRootWord
    else:
        return rootWord

def adjective_to_verb(sentence, index):
    newSentence = sentence.translate(str.maketrans('', '', string.punctuation))
    splitSentence = newSentence.split()
    word = splitSentence[index]
    transformedWord = word + 'en'
    
    return transformedWord