#!/usr/bin/env python

""" Assignment 2, Exercise 1, INF1340, Fall, 2015. Pig Latin

Test module for exercise1.py

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"


from exercise1 import pig_latinify


def test_basic():
    """
    Basic test cases from assignment hand out
    """
    assert pig_latinify("dog") == "ogday"
    assert pig_latinify("scratch") == "atchscray"
    assert pig_latinify("is") == "isyay"
    assert pig_latinify("apple") == "appleyay"


def test_advanced():
    assert pig_latinify('python') == 'ythonpay'
    assert pig_latinify('yooper') == 'ooperyay'
    assert pig_latinify('Youth') == 'outhyay'
    assert pig_latinify(' spacey ') == 'aceyspay'
    assert pig_latinify('supercallifragilisticexpialidocious'
                        ) == 'upercallifragilisticexpialidocioussay'


def test_bad_inputs():
    assert pig_latinify('12345') == 'Input error.'
    assert pig_latinify('two words') == 'Input error.'
    assert pig_latinify('c0mb1n3dw0rd') == 'Input error.'
    assert pig_latinify(12345) == 'Input error.'
    assert pig_latinify(["list", 1]) == 'Input error.'
