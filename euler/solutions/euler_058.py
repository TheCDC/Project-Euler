"""Spiral Primes
[Show HTML problem content]
Problem 58

Starting with
and spiralling anticlockwise in the following way, a square spiral with side length

is formed.

37 36 35 34 33 32 31
38 17 16 15 14 13 30
39 18  5  4  3 12 29
40 19  6  1  2 11 28
41 20  7  8  9 10 27
42 21 22 23 24 25 26
43 44 45 46 47 48 49

It is interesting to note that the odd squares lie along the bottom right diagonal, but what is more interesting is that
out of the numbers lying along both diagonals are prime; that is, a ratio of

.

If one complete new layer is wrapped around the spiral above, a square spiral with side length
will be formed. If this process is continued, what is the side length of the square spiral for which the ratio of primes along both diagonals first falls below

?
"""

from functools import cache
from euler.solutions.utils import isPrime


@cache
def corners(side_length):
    if side_length % 2 == 0:
        raise ValueError(f"{side_length=} must be odd")
    if side_length == 1:
        return (1, 1, 1, 1)
    if side_length <= 0:
        raise ValueError(f"{side_length=} less than zero")
    l = side_length - 1
    ret = corners(side_length - 2)
    out = [l * (index + 1) + ret[-1] for index, item in enumerate(ret)]
    return out


def nth_odd(n):
    return n * 2 + 1


def prime_corners(side_length):
    c = corners(side_length)
    np = sum(isPrime(cc) for cc in c)
    return np


def main():
    hits = 0
    for i in range(1, 1 + 2**32):
        side_length = nth_odd(i)
        np = prime_corners(side_length)
        hits += np
        ratio = hits / (side_length * 2 - 1)
        if ratio * 10 < 1:
            print(side_length, i, np, hits, ratio)
            return
        if i % 100000 == 0:
            print(i)


if __name__ == "__main__":
    main()
