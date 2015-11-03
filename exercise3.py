#!/usr/bin/env python

""" Assignment 2, Exercise 3, INF1340, Fall, 2015. DBMS

This module performs table operations on database tables
implemented as lists of lists.

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"


def compare_schemas(row1, row2):
    if row1 == row2:
        return True
    else:
        raise MismatchedAttributesException
        return False


def union(table1, table2):
    """
    Perform the union set operation on tables, table1 and table2.

    :param table1: a table (a List of Lists)
    :param table2: a table (a List of Lists)
    :return: the resulting table
    :raises: MismatchedAttributesException:
        if tables t1 and t2 don't have the same attributes
    """

    try:
        compare_schemas(table1[0], table2[0])
    except MismatchedAttributesException:
        print "Schemas do not match."
        return False

    union_list = []
    union_list.append(table1[0])

    for list_item in table1[1:]:
        if list_item not in table2[1:]:
            union_list.append(list_item)
    union_list += table2[1:]

    return union_list


def intersection(table1, table2):
    """
    Describe your function

    """

    try:
        compare_schemas(table1[0], table2[0])
    except MismatchedAttributesException:
        print "Schemas do not match."
        return False

    intersection_list = []
    intersection_list.append(table1[0])

    for list_item in table1[1:]:
        if list_item in table2[1:]:
            intersection_list.append(list_item)

    return intersection_list


def difference(table1, table2):
    """
    Describe your function

    """

    try:
        compare_schemas(table1[0], table2[0])
    except MismatchedAttributesException:
        print "Schemas do not match."
        return False

    difference_list = []
    difference_list.append(table1[0])

    for list_item in table1[1:]:
        if list_item not in table2[1:]:
            difference_list.append(list_item)

    return difference_list


#####################
# HELPER FUNCTIONS ##
#####################
def remove_duplicates(l):
    """
    Removes duplicates from l, where l is a List of Lists.
    :param l: a List
    """

    d = {}
    result = []
    for row in l:
        if tuple(row) not in d:
            result.append(row)
            d[tuple(row)] = True

    return result


class MismatchedAttributesException(Exception):
    """
    Raised when attempting set operations with tables that
    don't have the same attributes.
    """
    pass
