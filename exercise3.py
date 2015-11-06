#!/usr/bin/env python

""" Assignment 2, Exercise 3, INF1340, Fall, 2015. DBMS

This module performs table operations on database tables
implemented as lists of lists.

"""

__author__ = 'Isabelle Deluce and Tyler Harangozo'
__email__ = "isabelle.deluce@mail.utoronto.ca;tyler.harangozo@mail.utoronto.ca"
__copyright__ = "2015"
__license__ = "MIT License"


def compare_schemas(row1, row2):
    """
    Compare schemas of two tables

    :param row1: schema row of table1
    :param row2: schema row of table2
    :return: boolean of match
    :raises: MismatchedAttributesException if row1 != row2
    """
    if row1 == row2:
        return True
    else:
        raise MismatchedAttributesException


def union(table1, table2):
    """
    Perform the union set operation on tables, table1 and table2.

    :param table1: a table (a List of Lists)
    :param table2: a table (a List of Lists)
    :return: the resulting table
    :raises: MismatchedAttributesException if tables t1 and t2 don't have the
        same attributes
    """

    try:
        compare_schemas(table1[0], table2[0])
    except MismatchedAttributesException:
        raise MismatchedAttributesException

    union_list = []
    union_list.append(table1[0])

    for list_item in table1[1:]:
        if list_item not in table2[1:]:
            union_list.append(list_item)
    union_list += table2[1:]
    union_list = remove_duplicates(union_list)

    return union_list


def intersection(table1, table2):
    """
    Perform the intersection set operation on tables, table1 and table2.

    :param table1: a table (a List of Lists)
    :param table2: a table (a List of Lists)
    :return: the resulting table
    :raises: MismatchedAttributesException if tables t1 and t2 don't have the
        same attributes
    """

    try:
        compare_schemas(table1[0], table2[0])
    except MismatchedAttributesException:
        raise MismatchedAttributesException

    intersection_list = []
    intersection_list.append(table1[0])

    for list_item in table1[1:]:
        if list_item in table2[1:]:
            intersection_list.append(list_item)

    intersection_list = remove_duplicates(intersection_list)

    return intersection_list


def difference(table1, table2):
    """
    Describe your function

    Perform the difference set operation on tables, table1 and table2.

    :param table1: a table (a List of Lists)
    :param table2: a table (a List of Lists)
    :return: the resulting table
    :raises: MismatchedAttributesException if tables t1 and t2 don't have the
        same attributes
    """

    try:
        compare_schemas(table1[0], table2[0])
    except MismatchedAttributesException:
        raise MismatchedAttributesException

    difference_list = []
    difference_list.append(table1[0])

    for list_item in table1[1:]:
        if list_item not in table2[1:]:
            difference_list.append(list_item)

    difference_list = remove_duplicates(difference_list)

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