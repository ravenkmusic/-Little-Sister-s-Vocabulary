"""Functions for creating, transforming, and adding prefixes to strings."""
import string

def add_prefix_un(word):
    NewWord = "un" + word
    return NewWord


def make_word_groups(vocab_words):
    prefix = vocab_words[0]
    NewWords = f" :: {prefix}".join(vocab_words)
    return NewWords


def remove_suffix_ness(word):
    RootWord = word[:-4]
    if RootWord.endswith("i"):
        correctedRootWord = RootWord[:-1] + "y"
        print(correctedRootWord)
        return correctedRootWord
    else:
        return RootWord

def adjective_to_verb(sentence, index):
    NewSentence = sentence.translate(str.maketrans('', '', string.punctuation))
    splitSentence = NewSentence.split()
    word = splitSentence[index]
    transformedWord = word + 'en'
    
    return transformedWord