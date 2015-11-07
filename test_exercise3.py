#!/usr/bin/env python

""" Assignment 2, Exercise 3, INF1340, Fall, 2015. DBMS

Test module for exercise3.py

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"

from exercise3 import *

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

US_URBAN_AREAS = [["Name", "Population", "Area"],
                  ["Chicago", 9156000, 6856],
                  ["New York", 20630000, 11642],
                  ["Dallas", 6174000, 5175],
                  ["Los Angeles", 15058000, 6299],
                  ["Boston", 4478000, 5325]]

WORLD_URBAN_AREAS = [["Name", "Population", "Area"],
                     ["Tokyo", 37843000, 8547],
                     ["Mexico City", 20063000, 2072],
                     ["New York", 20630000, 11642],
                     ["Chicago", 9156000, 6856],
                     ["Toronto", 6456000, 2287]]

#####################
# HELPER FUNCTIONS ##
#####################


def is_equal(t1, t2):
    return sorted(t1) == sorted(t2)

###################
# TEST FUNCTIONS ##
###################


def test_union():
    """
    Test union operation.
    """

    result1 = [["Number", "Surname", "Age"],
               [7274, "Robinson", 37],
               [9297, "O'Malley", 56],
               [7432, "O'Malley", 39],
               [9824, "Darkes", 38]]

    result2 = [["Name", "Population", "Area"],
               ["Tokyo", 37843000, 8547],
               ["Mexico City", 20063000, 2072],
               ["Toronto", 6456000, 2287],
               ["Chicago", 9156000, 6856],
               ["New York", 20630000, 11642],
               ["Dallas", 6174000, 5175],
               ["Los Angeles", 15058000, 6299],
               ["Boston", 4478000, 5325]]

    assert is_equal(result1, union(GRADUATES, MANAGERS))
    assert is_equal(result2, union(WORLD_URBAN_AREAS, US_URBAN_AREAS))


def test_union_fail():
    """
    Test union on tables with mismatched attributes
    """
    result = [["Number", "Surname", "Age"],
              [7274, "Robinson", 37],
              [9297, "O'Malley", 56],
              [7432, "O'Malley", 39],
              [9824, "Darkes", 38]]
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
    result1 = [["Number", "Surname", "Age"],
               [7432, "O'Malley", 39],
               [9824, "Darkes", 38]]

    result2 = [["Name", "Population", "Area"],
               ["New York", 20630000, 11642],
               ["Chicago", 9156000, 6856]]

    assert is_equal(result1, intersection(GRADUATES, MANAGERS))
    assert is_equal(result2, intersection(WORLD_URBAN_AREAS, US_URBAN_AREAS))


def test_intersection_fail():
    """
    Test intersection on tables with mismatched attributes
    """
    result = [["Number", "Surname", "Age"],
              [7432, "O'Malley", 39],
              [9824, "Darkes", 38]]

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

    result1 = [["Number", "Surname", "Age"],
               [7274, "Robinson", 37]]

    result2 = [["Name", "Population", "Area"],
               ["Tokyo", 37843000, 8547],
               ["Mexico City", 20063000, 2072],
               ["Toronto", 6456000, 2287]]

    assert is_equal(result1, difference(GRADUATES, MANAGERS))
    assert is_equal(result2, difference(WORLD_URBAN_AREAS, US_URBAN_AREAS))


def test_difference_fail():
    """
    Test difference on tables with mismatched attributes
    """
    result = [["Number", "Surname", "Age"],
              [7274, "Robinson", 37]]

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
