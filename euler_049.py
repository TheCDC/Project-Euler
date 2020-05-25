"""
Project Euler Problem 49
========================

The arithmetic sequence, 1487, 4817, 8147, in which each of the terms
increases by 3330, is unusual in two ways: (i) each of the three terms are
prime, and, (ii) each of the 4-digit numbers are permutations of one
another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit
primes, exhibiting this property, but there is one other 4-digit
increasing sequence.

What 12-digit number do you form by concatenating the three terms in this
sequence?
"""
from utils import prime_sieve
from collections import Counter
from itertools import combinations


def count_permutations():
    # start by generating primes
    mymap = dict()

    for p in prime_sieve(10000):
        # minimum digits
        if len(str(p)) < 4:
            continue
        # associate all primes with the same multisets of digits.
        key = ''.join(sorted(str(p)))
        if key in mymap:
            mymap[key].append(p)
        else:
            mymap.update({key: [p]})

    for k in mymap:
        # Take primes the equal multisets of digits three at a time to find the second 3-sequence.
        # Some 'families' have more than 3 members so take combinations three at a time
        # and check for a constant delta between those primes.
        for comb in combinations(mymap[k], 3):

            s = list(sorted(comb))

            delta = s[1] - s[0]
            for i in range(1, len(s)):
                if s[i] - s[i-1] != delta:
                    break
            else:
                yield s


def main():
    known = set([1487, 4817, 8147])
    ps = list(count_permutations())
    for p in ps:
        if set(p) != known:
            print(''.join(map(str, p)))


if __name__ == '__main__':
    main()
