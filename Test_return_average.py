import pytest

from Return_average_function import return_average
from Return_average_function import return_max_number
from Return_average_function import Listcalculations

def test_average_basic():
	assert return_average([2,2]) == 2.0

def test_average_zeros():
	assert return_average([]) == 0.0

def test_return_max_number():
		assert return_max_number([9,3,5,1,5,7]) == 9


def test_list_sum():
    assert Listcalculations.list_sum([1, 2, 3]) == 6

    with pytest.raises(ValueError) as info:
        Listcalculations.list_sum([])
    assert str(info.value) == 'List cannot be empty'

    with pytest.raises(ValueError) as info1:
        Listcalculations.list_sum([1])
    assert str(info1.value) == 'List has to contain two numbers!'


