#!/usr/bin/env python

""" Assignment 2, Exercise 1, INF1340, Fall, 2015. Pig Latin

This module converts English words to Pig Latin words

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"


def pig_latinify(word):
    """
    Describe your function

    :param : word (string)
    :return: the word translated into piglatin
    :raises: AttributeError: if word is not entirely alphabetical or lower case

    """
    result = ""

    vowels = ["a", "e", "i", "o", "u", "y"]

    # sanitize input
    if(type(word) is str):
        word = word.strip()
        try:
            if (word.isalpha() is False):
                return "Input error."
            else:
                word = word.lower()
        except AttributeError:
            return "Input error."
    else:
        return "Input error."

    # get first letter type
    if(word[0] in vowels):
        first_type = "v"  # vowel condition
        if(word[0] == "y"):
            first_type = "c"  # treat y as consonant when beginning word
            vowels.pop()  # remove y from the list of vowels
    else:
        first_type = "c"  # consonant condition

    # convert word to pig latin
    if(first_type == "v"):
        result = word + "yay"
    elif(first_type == "c"):
        i = 0
        word_len = len(word)
        while word[i] not in vowels:
            i += 1
        slice_start = i
        result = word[slice_start:word_len] + word[0:slice_start] + "ay"

    return result
