#!/usr/bin/env python3
"""Pentagon numbers
Problem 44

Pentagonal numbers are generated by the formula, Pn=n(3n−1)/2. The first ten pentagonal numbers are:

1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...

It can be seen that P4 + P7 = 22 + 70 = 92 = P8. However, their difference, 70 − 22 = 48, is not pentagonal.

Find the pair of pentagonal numbers, Pj and Pk, for which their sum and difference are pentagonal and D = |Pk − Pj| is minimised; what is the value of D?

"""


def quadratic(a, b, c) -> float:
    sq = (b**2 - 4 * a * c)**(1 / 2)
    denom = 2 * a
    return max(((-b + sq) / denom, (-b - sq) / denom))


def pn(n) -> float:
    """nth pentagonal number"""
    return n * (3 * n - 1) / 2


def np(p) -> float:
    """n, given pentagonal number.
        If p is not a true pentagonal number
    then output will be a fraction."""
    return quadratic(3 / 2, -1 / 2, -p)


def test(pa, pb) -> bool:
    """Sum and difference of a and b are both pentagonal?"""
    return np(pa + pb) % 1 == 0 and np(abs(pa-pb)) % 1 == 0


def main():
    # check all combinations of integers A and B with an increasing upper bound
    # until the sum and difference of A and B are pentagonal
    a = 0
    while True:
        a += 1

        for b in range(a, 0, -1):
            pa, pb = pn(a), pn(b)
            if test(pa, pb):
                # print(a,b,abs(a-b))
                print(abs(int(pa - pb)))
                print(a, b, np(a), np(b))
                quit()


if __name__ == '__main__':
    main()
