import json
import os, sys

def load_words(file):
    try:
        filename = os.path.join(os.getcwd(), str(file))
        with open(filename,"r") as english_dictionary:
            valid_words = json.load(english_dictionary)
            return valid_words
    except Exception as e:
        return str(e)

def check_word(s):
    try:
        if (english_words[str(s)] > 0):
            return True
        else:
            return False
    except KeyError:
        return False

def define_words(file):
    global english_words
    try:
        if (not isinstance(english_words, dict)):
            english_words = load_words(file)
    except NameError:
        english_words = load_words(file)

if __name__ == '__main__':
    define_words("words_dictionary.json")
