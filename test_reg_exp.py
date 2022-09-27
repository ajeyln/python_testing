import pytest

from reg_exp import Filename

def test_initiate():
    expected_value = "text1.txt"
    obj1 = Filename("text1.txt")
    actual_value = obj1.filename
    assert actual_value == expected_value

    