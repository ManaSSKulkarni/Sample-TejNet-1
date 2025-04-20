"""Pytest"""

import pytest
from sample4 import add, concatenation, reverse_array, Calculator


def test_add():
    """Addition"""
    res = add(1, 2)
    assert res == 3


def test_concatenation():
    """Concatenation"""
    res = concatenation("Hello", "World")
    assert res == "HelloWorld"
    assert res.startswith("H")
    assert res.endswith("d")


def test_reverse():
    """Reversing Array"""
    res = reverse_array([5, 4, 3, 2, 1])
    assert res == [1, 2, 3, 4, 5]


def test_notequal():
    """Samole test"""
    res = add(1, 3)
    assert res != 2


@pytest.fixture
def sample_data_fixture():
    """Sample data"""
    return [1, 2, 3]


def test_fixture(sample_data_fixture):
    """Sample test fixture"""
    assert len(sample_data_fixture) == 3


@pytest.fixture
def calc_fixture():
    """Calculator instance"""
    return Calculator()


@pytest.mark.parametrize("number,result", [(2, 4), (3, 9), (4, 16)])
def test_square(calc_fixture, number, result):
    """Calling method"""
    assert calc_fixture.square(number) == result


@pytest.mark.skip(reason="Unknown")
def test_example():
    """Example"""
    assert False


def test_divide(mocker):
    """Division"""
    calc2 = Calculator()
    mocker.patch.object(Calculator, "multiply", return_value=10)
    assert calc2.divide(20, 2) == 10


if __name__ == "__main__":
    pytest.main()
