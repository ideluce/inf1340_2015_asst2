#!/usr/bin/env python

""" Assignment 2, Exercise 3, INF1340, Fall, 2015. DBMS

Test module for exercise3.py

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"

from exercise3 import union, intersection, difference, MismatchedAttributesException


###########
# TABLES ##
###########
STUDENTS = [["Number", "Surname", "Age", "GradYear"],
            [7274, "Robinson", 37, 2010],
            [7432, "O'Malley", 39, 2012],
            [9824, "Darkes", 38, 2015]]

GRADUATES = [["Number", "Surname", "Age"],
             [7274, "Robinson", 37],
             [7274, "Robinson", 37],
             [7432, "O'Malley", 39],
             [9824, "Darkes", 38]]

MANAGERS = [["Number", "Surname", "Age"],
            [9297, "O'Malley", 56],
            [9297, "O'Malley", 56],
            [7432, "O'Malley", 39],
            [9824, "Darkes", 38]]

EMPLOYEES = [["Surname", "Number", "Age"],
             ["O'Malley", 9297, 56],
             ["O'Malley", 9297, 56],
             ["O'Malley", 7432, 39],
             ["Darkes", 9824, 38]]

#####################
# HELPER FUNCTIONS ##
#####################


def is_equal(t1, t2):
    return set(map(tuple, t1)) == set(map(tuple, t2))


###################
# TEST FUNCTIONS ##
###################
def test_union():
    """
    Test union operation.
    """

    result = [["Number", "Surname", "Age"],
              [7274, "Robinson", 37],
              [9297, "O'Malley", 56],
              [7432, "O'Malley", 39],
              [9824, "Darkes", 38]]

    assert is_equal(result, union(GRADUATES, MANAGERS))

    try:
        is_equal(result, union(GRADUATES, STUDENTS))
    except MismatchedAttributesException:
        assert True
    else:
        assert False
    
    try:
        is_equal(result, union(EMPLOYEES, MANAGERS))
    except MismatchedAttributesException:
        assert True
    else:
        assert False

def test_intersection():
    """
    Test intersection operation.
    """
    result = [["Number", "Surname", "Age"],
              [7432, "O'Malley", 39],
              [9824, "Darkes", 38]]

    assert is_equal(result, intersection(GRADUATES, MANAGERS))

    try:
        is_equal(result, intersection(GRADUATES, STUDENTS))
    except MismatchedAttributesException:
        assert True
    else:
        assert False

    try:
        is_equal(result, intersection(EMPLOYEES, MANAGERS))
    except MismatchedAttributesException:
        assert True
    else:
        assert False

def test_difference():
    """
    Test difference operation.
    """

    result = [["Number", "Surname", "Age"],
              [7274, "Robinson", 37]]

    assert is_equal(result, difference(GRADUATES, MANAGERS))

    try:
        is_equal(result, difference(GRADUATES, STUDENTS))
    except MismatchedAttributesException:
        assert True
    else:
        assert False

    try:
        is_equal(result, difference(EMPLOYEES, MANAGERS))
    except MismatchedAttributesException:
        assert True
    else:
        assert False
