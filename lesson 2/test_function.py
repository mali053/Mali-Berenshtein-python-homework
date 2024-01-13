import pytest
import main


@pytest.mark.parametrize('num, num1, result', [(1, 6, {1, 2, 3, 5}), (3, 9, {3, 5, 7}), (3, 15, {3, 5, 7, 11, 13})])
def test_find_prime(num, num1, result):
    assert main.find_primes(num, num1) == result


@pytest.mark.parametrize("list1, result",
                         [([1, 2, 3, 4, 57, 5, 4, 1], [1, 1, 2, 3, 4, 4, 5, 57]), ([12, 5, 9], [5, 9, 12])])
def test_sort_list(list1, result):
    assert main.sort_list(list1) == result


@pytest.mark.parametrize('str, result', [("1+3", 4), ("9/3", 3), ("2*8", 16)])
def test_calculate_expression(str, result):
    assert main.calculate_expression(str) == result
