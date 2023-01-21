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
from euler.solutions.utils import TimingContext

from itertools import combinations, permutations
from typing import List

PANDIGITAL_SET = set(range(1, 10))


def generate_pandigitals():
    yield from permutations(reversed(range(1, 10)))


def is_pandigital(n: int):
    str_n = str(n)
    set_n = set([int(d) for d in str_n])
    return len(str_n) == 9 and set_n == PANDIGITAL_SET


def get_product(n: int, i: int):
    return int("".join(map(str, (i * nn for nn in range(1, n + 1)))))


def check_n_i(n: int, i: int):
    product = get_product(n, i)
    return is_pandigital(product)


def generate_products():
    n_to_bounds_i = {
        2: (5000, 9999),
        3: (100, 999),
        4: (1, 32),
        5: (1, 10),
        6: (1, 3),
        9: (1, 9),
    }
    largest_pandigital = None
    iterations = 0
    for n, bounds_i_inclusive in n_to_bounds_i.items():
        for i in range(bounds_i_inclusive[0], bounds_i_inclusive[1] + 1):
            product = (get_product(n, i), n, i)
            valid = is_pandigital(product[0])
            if valid:
                print(iterations, product)
                largest_pandigital = (
                    max(largest_pandigital, product, key=lambda l: l[0])
                    if largest_pandigital
                    else product
                )
            iterations += 1
    return (iterations, largest_pandigital)


if __name__ == "__main__":
    print(check_n_i(3, 192))
    assert check_n_i(3, 192)
    assert check_n_i(5, 9)
    for p in zip(generate_pandigitals(), range(10)):
        print(p)
    with TimingContext(silent=False) as tc:
        iterations, largest = generate_products()
    print(
        f"solution found after {iterations} iterations: {largest[0]} n={largest[1]} i={largest[1]}"
    )
