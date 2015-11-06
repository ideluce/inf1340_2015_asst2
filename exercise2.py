#!/usr/bin/env python

""" Assignment 2, Exercise 2, INF1340, Fall, 2015. DNA Sequencing

This module converts performs substring matching for DNA sequencing

"""

__author__ = 'Isabelle Deluce and Tyler Harangozo'
__email__ = "isabelle.deluce@mail.utoronto.ca;tyler.harangozo@mail.utoronto.ca"
__copyright__ = "2015"
__license__ = "MIT License"


def find(input_string, substring, start, end):
    """
    Function to find the index of the first occurence of a string within a
        substring of an input string

    :param : input_string (string), substring (string), start (int), end (int)
    :return: match_start (int)

    """
    search_area = input_string[start:end]

    i = 0
    match_start = -1

    while i < len(search_area)-(len(substring)-1):  # stop search if past end
        letter = search_area[i]

        if letter == substring[0]:
            j = i + 1  # j and k are +1 since already found first match above
            k = 1
            while k < len(substring):
                if substring[k] == search_area[j]:
                    if k == len(substring)-1:
                        match_start = i + start
                        return match_start  # short circuit if complete match
                    j += 1
                    k += 1
                else:
                    match_start = -1
                    k = len(substring)  # end while loop early
        i += 1

    return match_start
find(input_string, substring, 0, end)

def multi_find(input_string, substring, start, end):
    """
    Function to find the indexes of all occurrences of a string within a
        substring of an input string

    :param : input_string (string), substring (string), start (int), end (int)
    :return: starting indexes of input_string where substring is found
            as string, separated by commas

    """
    result = ""
    i = start
    j = i
    while(i < end):
        substring_check = find(input_string, substring, j, end)

        if substring_check != -1:
            latestindex = substring_check
            result += str(latestindex) + ","
            j = latestindex + 1

        i += 1
    result = result.rstrip(",")
    return result