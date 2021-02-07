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
    n = 0
    p = 1
    for digit, radix in zip(digits, radixes):
        n = n * radix + digit
    return n


def unpack(n: int, radixes: List[int]) -> List[int]:
    digits = []
    for r in radixes:
        digits.append(n % r)
        n = n // r
    return digits


def choose_by_unpacked(unpacked: List[int], alphabet: List):
    l = list((alphabet))
    out = []
    for up in unpacked:
        out.append(l.pop(up))
    return list((out))


if __name__ == "__main__":
    assert choose_by_unpacked(unpack(1, [1, 2, 3]), "abc") == ["a", "c", "b"]
