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
    assert find("This is an ex-parrot", "THIS", 0, 20) == -1
    assert find("This is ex-parrot number 123", "123", 0, 28) == 25


def test_multi_find_basic():
    """
    Test multi_find function.
    """
    assert multi_find("Ni! Ni! Ni! Ni!", "Ni", 0, 20) == "0,4,8,12"
    assert multi_find("Ni! No! No! Ni!", "Ni", 0, 20) == "0,12"
    assert multi_find("Ni! Ni! Ni! No!", "Ni", 0, 20) == "0,4,8"
    assert multi_find("11! Ni! 11! Ni!", "11", 0, 20) == "0,8"
    assert multi_find("NI! Ni! NI! Ni!", "NI", 0, 20) == "0,8"
    assert multi_find("ni! ni! ni! ni!", "ni", 0, 20) == "0,4,8,12"
