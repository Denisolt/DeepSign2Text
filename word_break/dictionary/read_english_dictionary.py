import json
import os, sys

def load_words():
    try:
        filename = os.path.join(os.getcwd(), "words_dictionary.json")
        with open(filename,"r") as english_dictionary:
            valid_words = json.load(english_dictionary)
            return valid_words
    except Exception as e:
        return str(e)

def check_word(s):
    try:
        if (english_words[str(s)] is 1):
            return True
    except KeyError:
        return False

if __name__ == '__main__':
    try:
        if (not isinstance(english_words, dict)):
            english_words = load_words();
    except NameError:
        english_words = load_words();
