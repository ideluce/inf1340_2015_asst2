#!/usr/bin/env python

""" Assignment 2, Exercise 2, INF1340, Fall, 2015. DNA Sequencing

This module converts performs substring matching for DNA sequencing

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"


def find(input_string, substring, start, end):
    """
    Describe your function

    :param :
    :return:
    :raises:

    """

    search_area = input_string[start:end]

    i = 0
    match_start = -1
    in_match = False
    while i < (len(search_area)-1):
        letter = search_area[i]
        if in_match is False:
            if letter == substring[0]:
                in_match = True
                restart_i = i
                j = 0
                match_start = i + start
                j += 1
        elif in_match is True and j < len(substring):
            if letter != substring[j]:
                in_match = False
                match_start = -1
                i = restart_i
            j += 1
        elif in_match is True and j == len(substring):
            return match_start
        i += 1

    return match_start

def multi_find(input_string, substring, start, end):
    """
    Describe your function

    :param :
    :return:
    :raises:

    """
    result = ""
    i = start
    j = i
    while(i < end):
        if (find(input_string, substring, j, end) != -1):
            latestindex = find(input_string, substring, j, end)
            result += str(latestindex)+","
            j = latestindex+1
        i += 1
    result = result.rstrip(",")
    return result
