#!/usr/bin/env python

""" Assignment 2, Exercise 2, INF1340, Fall, 2015. DNA Sequencing

Test module for exercise2.py

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"

from exercise2 import find, multi_find


def test_find_basic():
    """
    Test find function.
    """
    assert find("This is an ex-parrot", "parrot", 0, 20) == 14
    assert find("This is an ex-parrot", "an", 0, 20) == 8
    assert find("This is an ex-parrot", "This", 0, 20) == 0
    assert find("This is an ex-parrot", "this", 0, 20) == -1
    assert find("This is an ex-parrot", "THIS", 0, 20) == -1


def test_multi_find_basic():
    """
    Test multi_find function.
    """
    assert multi_find("Ni! Ni! Ni! Ni!", "Ni", 0, 20) == "0,4,8,12"
    assert multi_find("Ni! No! No! Ni!", "Ni", 0, 20) == "0,12"
    assert multi_find("Ni! Ni! Ni! No!", "Ni", 0, 20) == "0,4,8"
    assert multi_find("Ni! Ni! Ni! Ni!", "Hi", 0, 20) == ""
    assert multi_find("12! Ni! Ni! 12!", "12", 0, 20) == "0,12"
    assert multi_find("Ni! Ni! Ni! Ni!", "NI", 0, 20) == ""
    assert multi_find("Ni! Ni! Ni! Ni!", "ni", 0, 20) == ""
    assert multi_find("ATCGGGGTGCGCGGGGAT", "GGGG", 0, 23) == "3,12"
    assert multi_find("ATCGGGGTGCGCGGGGAT", "GGGG", 6, 23) == "12"
    assert multi_find("ATCGGGGTGCGCGGGGAT", "GGGG", 0, 13) == "3"
    assert multi_find("ATCGGGGTGCGCGGGGAT", "GGGG", 6, 13) == ""
    assert multi_find("ATCGGGGTGCGCGGG", "GGGG", 0, 23) == "3"

