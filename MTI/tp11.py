#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Programme d'analyse de texte - TP Python

import re
import sys

# --------------------------------------------
def clean_text(text):
    """
    Remove punctuation from a text.
    """
    punct = "+.*/?,;\'#"
    for p in punct:
        text = text.replace(p, "")
    return text


# --------------------------------------------
def tokenize(text):
    """
    Convert text into tokens, return a list of tokens (words).
    """
    return text.split()


# --------------------------------------------
def tokenize2(text):
    """
    Convert text into tokens using regular expressions.
    """
    spaces = r"\s+"
    words = re.split(spaces, text)
    return words


# --------------------------------------------
def word_freq(words):
    """
    Count words and return a dictionary of words with their occurrences.
    """
    index = {}
    for w in words:
        if w in index:
            index[w] += 1
        else:
            index[w] = 1
    return index


# --------------------------------------------
def most_common_word(words_freq_table):
    """
    Find the most frequent word and its number of occurrences.
    """
    frequent = ""
    frequency = 0
    for word in words_freq_table:
        if words_freq_table[word] > frequency:
            frequent = word
            frequency = words_freq_table[word]
    return frequent


# --------------------------------------------
def read_file(filename):
    """
    Read a text from a file and return its content.
    """
    text = ""
    try:
        fl = open(filename, "r", encoding="utf-8")
    except:
        print("Can't open file:", filename)
        sys.exit()
    # if success
    text = fl.read()
    fl.close()
    return text


# --------------------------------------------
def main():
    text = """Surprise steepest recurred landlord mr wandered amounted of.
    Continuing devonshire but considered its. Rose past oh shew roof
    is song neat. Do depend better praise do friend garden an wonder to.
    Intention age nay otherwise but breakfast. Around garden beyond to extent by."""

    # Nettoyage
    text = clean_text(text)
    print("Texte nettoyé:\n", text)

    # Tokenisation
    words = tokenize(text)
    print("\nListe des mots:\n", words)

    # Comptage
    words_nb = word_freq(words)
    print("\nDictionnaire des fréquences:\n", words_nb)

    # Lecture depuis un fichier
    data = read_file("data.txt")
    print("\nContenu du fichier data.txt:\n", data)

    # Nouveau comptage sur le fichier
    words2 = tokenize(data)
    word_freq_table = word_freq(words2)

    print("\nFréquences des mots dans le fichier:\n", word_freq_table)

    # Mot le plus fréquent
    freqw = most_common_word(word_freq_table)
    print("\nMost frequent word is:", freqw, "-", word_freq_table[freqw])

    return 0


# --------------------------------------------
if __name__ == "__main__":
    main()
