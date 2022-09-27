import pytest

from inher_eg import Employee
from inher_eg import Person

def test_person_initiate():
    obj1 = Person("Ajey", 101)
    expected_value1 = "Ajey"
    actual_value1 = obj1.name
    assert actual_value1 == expected_value1
    expected_value2 = 101
    actual_value2 = obj1.idnumber
    assert actual_value2 == expected_value2

def test_person_display():
    obj1 = Person("Ajey", 101)
    expected_value1 = ('Ajey', 101)
    actual_value1 = obj1.display()
    assert actual_value1 == expected_value1

def test_employee_initiate():
    obj2 = Employee("Ajey", 101, 100000, "CEO")
    expected_value1 = "Ajey"
    actual_value1 = obj2.name
    assert actual_value1 == expected_value1
    expected_value2 = 101
    actual_value2 = obj2.idnumber
    assert actual_value2 == expected_value2
    expected_value3 = 100000
    actual_value3 = obj2.salary
    assert actual_value3 == expected_value3
    expected_value4 = "CEO"
    actual_value4 = obj2.post
    assert actual_value4 == expected_value4



    
