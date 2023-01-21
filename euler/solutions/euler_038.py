"""
Project Euler Problem 38
========================

Take the number 192 and multiply it by each of 1, 2, and 3:

  192 * 1 = 192
  192 * 2 = 384
  192 * 3 = 576

By concatenating each product we get the 1 to 9 pandigital, 192384576. We
will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4,
and 5, giving the pandigital, 918273645, which is the concatenated product
of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as
the concatenated product of an integer with (1,2, ... , n) where n > 1?
"""


"""5000 <= x <= 10,000


"""


from itertools import combinations, permutations
from typing import List

PANDIGITAL_SET = set(range(1, 10))


def generate_pandigitals():
    yield from permutations(set(range(1, 10)))


def is_pandigital(n: int):
    sn = str(n)
    return len(sn) == 9 and len(set(sn)) == 9


def check_n_i(n: int, i: int):
    return is_pandigital(int("".join(map(str, (i * nn for nn in range(1, n + 1))))))


if __name__ == "__main__":
    assert check_n_i(3, 192)
    assert check_n_i(5, 9)
