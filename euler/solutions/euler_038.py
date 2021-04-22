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


def is_match(x, n):
    digits = set("".join(str(x * i) for i in range(1, n + 1)))
    return len(digits) == 9


def x_satisfies(x):
    return any(is_match(x, n) for n in range(2, 9 + 1))


def generate_xs():
    for ds in permutations(list(range(1, 10)), 4):
        yield int("".join(map(str, ds)))


def pandigital_satisfies(p) -> bool:
    """is there an x that generates this pandigital with any n>1?"""
    for n in range(2, 9 + 1):
        parts = [p / z for z in range(1, n + 1)]
        # parts must be all the same integers
        if len(set(parts)) == 1:
            return n
    return 0


def get_digit_groupings(pandigital: int, n: int) -> List[List[int]]:
    if n == 1:
        return [[pandigital]]
    elif n == 9:
        return [list(map(int, list(str(pandigital))))]


def concat_digit_groups(digit_groups: List[int]) -> int:
    return int("".join([str(n) for n in digit_groups]))


if __name__ == "__main__":
    MAX = 999999999
    for i in range(MAX):
        if i % 1000000000 == 0:
            print("PROGRESS", i, i / MAX)
        for n in range(1, 10):
            digit_groups = [i * subn for subn in range(1, n + 1)]
            concatenated = concat_digit_groups(digit_groups)
            if concatenated > MAX:
                continue
            digits = set(int(x) for x in str(concatenated))
            if digits == PANDIGITAL_SET:
                print(i, concatenated, n)
    assert pandigital_satisfies(192384576) == True
    assert pandigital_satisfies(918273645) == True
    # m = 0
    # for p in generate_pandigitals(9):
    #     p = int("".join(map(str, p)))
    #     s = pandigital_satisfies(p)
    #     if s > 0:
    #         m = max(m, p)
    #         print(p, s)
    # print(m)
