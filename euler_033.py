"""
Project Euler Problem 33
========================

The fraction 49/98 is a curious fraction, as an inexperienced
mathematician in attempting to simplify it may incorrectly believe that
49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less
than one in value, and containing two digits in the numerator and
denominator.

If the product of these four fractions is given in its lowest common
terms, find the value of the denominator.
"""
from typing import List


def is_trivial(f):
    return f[0] % 10 == 0 and f[1] % 10 == 0


def shared_digits(f):
    numerator = f[0]
    denominator = f[1]
    return set(str(numerator)) & set(str(denominator))


def can_cancel(f):
    return len(shared_digits(f)) > 0


def delete_digit(n, d):
    ds = list(str(n))
    ds.remove(str(d))
    return int(''.join(ds))


def cancel(f: List[int]):
    for d in shared_digits(f):
        newf = (delete_digit(f[0], d), delete_digit(f[1], d))
        if newf[1] > 0:
            yield newf


def generate_fractions():
    for i in range(10, 99+1):
        for j in range(i+1, 99+1):
            f = (i, j)
            if can_cancel(f) and not is_trivial(f):
                yield f


def find_all_examples():
    for f in generate_fractions():
        for c in cancel(f):
            if c[0]/c[1] == f[0]/f[1]:
                # print(f, c)
                yield f


def main():
    for f in find_all_examples():
        print(f)


if __name__ == '__main__':
    main()
