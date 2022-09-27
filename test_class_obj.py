import pytest

from class_obj import Complex
from class_obj import addition

def test_initiate():
    obj1 = Complex(2,12)
    expected_real_value = 2
    actual_real_value = obj1.r
    expected_imaginary_value = 12 
    actual_imaginary_value = obj1.i
    assert actual_real_value == expected_real_value
    assert actual_imaginary_value == expected_imaginary_value

def test_display():
    obj1 = Complex(2,12)
    expected_value = '2+i12'
    actual_value = obj1.display()
    assert actual_value == expected_value

def test_getrealno():
    obj1 = Complex(4,5)
    expected_value = 4
    actual_value = obj1.getrealno()
    assert actual_value == expected_value

def test_getimgno():
    obj1 = Complex(4,5)
    expected_value = 5
    actual_value = obj1.getimgno()
    assert actual_value == expected_value

def test_setrealno():
    obj1 = Complex(5,6)
    expected_value = 10
    actual_value = obj1.setrealno(10)
    assert actual_value == expected_value

def test_setimgno():
    obj1 = Complex(5,6)
    expected_value = 7
    actual_value = obj1.setimgno(7)
    assert actual_value == expected_value

def test_addition():
    obj1 = Complex(3,4)
    obj2 = Complex(7,8)
    expected_value = '10+i12'
    actual_value = obj1.addition(obj2)
    assert actual_value == expected_value

def testing_addition():
    obj1 = Complex(2,5)
    obj2 = Complex(6,3)
    expected_value = '8+i8'
    actual_value = addition(obj1,obj2)
    assert actual_value == expected_value