#!/usr/bin/env python

""" Assignment 2, Exercise 2, INF1340, Fall, 2015. DNA Sequencing

Test module for exercise2.py

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"

from exercise2 import find, multi_find
print True if "t" == "T" else False

def test_find_basic():
    """
    Test find function.
    """
    assert find("This is an ex-parrot", "parrot", 0, 20) == 14
    assert find("actggggtttt", "actg", 0, 10) == 0
    assert find("actggggtttt", "tttt", 0, 10) == 7
    assert find("actggggtttt", "TTTT", 0, 10) == -1
    assert find("ACTGGGGTTTT", "tttt", 0, 10) == -1
    assert find("actgg1234", "1234", 0, 8) == 5

def test_multi_find_basic():
    """
    Test multi_find function.
    """
    assert multi_find("Ni! Ni! Ni! Ni!", "Ni", 0, 20) == "0,4,8,12"
    assert find("actggggtttt", "actg", 0, 10) == 0
    assert find("actggggtttt", "tttt", 0, 10) == 7
    assert find("actggggtttt", "TTTT", 0, 10) == -1
    assert find("ACTGGGGTTTT", "tttt", 0, 10) == -1
    assert find("actgg1234", "1234", 0, 8) == 5

