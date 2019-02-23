#!/usr/bin/env python3
"""
Project Euler Problem 23
========================

A perfect number is a number for which the sum of its proper divisors is
exactly equal to the number. For example, the sum of the proper divisors
of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect
number.

A number whose proper divisors are less than the number is called
deficient and a number whose proper divisors exceed the number is called
abundant.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the
smallest number that can be written as the sum of two abundant numbers is
24. By mathematical analysis, it can be shown that all integers greater
than 28123 can be written as the sum of two abundant numbers. However,
this upper limit cannot be reduced any further by analysis even though it
is known that the greatest number that cannot be expressed as the sum of
two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the
sum of two abundant numbers.
===================
What can be said about the sum of two adundant numbers?

"""
import utils


def is_abundant(n):
    # import pudb; pudb.set_trace()
    ds = utils.divisors(n)
    ds.remove(n)  # keep only proper divisors
    return sum(ds) > n


def problem():
    # given: upper bound is 28123
    upper_bound = 28123
    abundants = [i for i in range(1, upper_bound + 1) if is_abundant(i)]

    print(f'Found {len(abundants)} abundant numbers less than {upper_bound}')

    all_candidates = set(range(upper_bound + 1))
    for idxa, a in enumerate(abundants):
        for b in abundants[idxa:len(abundants)]:
            if a + b > upper_bound:
                break
            try:
                all_candidates.remove(a + b)
            except KeyError:
                pass
    # print('\n'.join(map(str, list(all_candidates))))
    # print(len(all_candidates))
    return sum(all_candidates)


def main():
    print(problem())


if __name__ == '__main__':
    main()
