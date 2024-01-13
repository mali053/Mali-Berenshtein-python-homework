import pytest


def find_primes(start, end):
    primes = set(range(start, end))
    k = 2

    while k < end:
        for number in set(primes) - set([k]):
            if (number % k) == 0:
                primes.remove(number)

        k += 1

    return primes


def sort_list(list1):
    return sorted(list1)


def calculate_expression(str1):
    return eval(str1)


# print(find_primes(3, 100))
