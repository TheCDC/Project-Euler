"""
Project Euler Problem 24
========================

A permutation is an ordered arrangement of objects. For example, 3124 is
one possible permutation of the digits 1, 2, 3 and 4. If all of the
permutations are listed numerically or alphabetically, we call it
lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

                    012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3,
4, 5, 6, 7, 8 and 9?
"""


from typing import List


def pack(digits: List[int], radixes: List[int]) -> int:
    """Take a list of numerals and accompanying radixes.

    Returns magnitude of the number they represent."""
    n = 0
    for digit, radix in zip(digits, radixes):
        n = n * radix + digit
    return n


def unpack(n: int, radixes: List[int]) -> List[int]:
    """Take a magnitude and a list of radixes.

    Returns the digits of the mixed-radix number."""
    digits = []
    for r in reversed(radixes):
        digits.insert(0, n % r)
        n = n // r
    return digits


def nth_permutation(tokens: List, index: int, radixes: List[int]):
    choice_indices = unpack(index, radixes)
    ts = list(tokens)  # copy list of tokens
    out = [ts.pop(i) for i in choice_indices]
    return out


if __name__ == "__main__":
    # print(unpack(999999, [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
    print(
        *nth_permutation(list(range(10)), 999999, [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]),
        sep=""
    )
