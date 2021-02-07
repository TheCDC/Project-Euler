#!/usr/bin/env python3
"""
Digit factorials
Problem 34

145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.


==========
There are a finite number of them so there must be a cutoff.
Conjecture: no base-10 number with more than 8 digits can satisfy the stated property.
9! = 362880
9!*8 = 2,903,040
9!*8 < 99,999,999

Consider the number 9. As you add 9s to the end n_next = n*10+9 while f(n_next) = n+9!
"""

from euler.solutions.utils import fact, numDigits, nthDigit
from timeit import default_timer
from functools import lru_cache


@lru_cache(maxsize=10)
def fact_memoized(n):
    return fact(n)


@lru_cache(maxsize=1024)
def dfsum(n):
    s = 0
    sn = str(n)
    for d in sn:
        s += fact_memoized(int(d))

    return s


def is_match(n):
    s = 0
    if n < 10:
        return False
    sn = str(n)
    for idx, d in enumerate(sn):
        s += fact_memoized(int(d))
        # if s has already surpassed n
        if s > n:
            return False
        # if s can't grow fast enough to catch with with n as we traverse the digits
        if s + fact_memoized(9) * (len(sn) - idx) < n:
            return False
    return s == n


DIGITS = "1234567890"

bad = set()


def generate_matches(s=""):
    if s in bad:
        return
    if len(s) > 8:
        return
    # print(s)

    n = int(s) if s != "" else 0
    if is_match(n):
        yield s

    for d in DIGITS:
        s_next = s + d
        n_next = int(s_next)
        digit_fact_sum_next = dfsum(n_next)
        # digit fact sum already too big
        if digit_fact_sum_next > fact_memoized(9) * 7:
            bad.add(s)
            continue
        # digit fact sum can't catch up
        if n_next * 10 > n_next + fact_memoized(9):
            bad.add(s)
            continue
        yield from generate_matches(s_next.lstrip("0"))


def nines():
    n = 1
    while True:
        yield int("9" * n)
        n += 1


def test(n):
    return dfsum(n) == n


def main2():
    for m in generate_matches():
        print("FOUND", m)


def main():
    assert is_match(145), "yikes"
    start_time = default_timer()
    # print(test(145))
    # find an upper bound on num of digits
    ndigits = 1
    found = 0
    for digit_string in nines():
        if dfsum(int("1" * len(str(digit_string)))) > digit_string:
            continue
        if dfsum(digit_string) < digit_string:
            found = digit_string
            break
    # print(found, 'max digits=', len(str(found)))
    upper_bound = 10 ** (len(str(found)))
    s = 0
    for n in range(1, upper_bound):
        # for n in range(10**7, 2*10**7):
        if is_match(n):
            # print('FOUND', n)
            s += n
        elif n % 1000000 == 0:
            # print('progress', n, default_timer() - start_time)
            pass
    print(s)


if __name__ == "__main__":
    main()
