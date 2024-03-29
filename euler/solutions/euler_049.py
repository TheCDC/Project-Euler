"""
Project Euler Problem 49


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
from euler.solutions.utils import TimingContext
from euler.solutions.utils import prime_sieve
from collections import Counter
from itertools import combinations


def count_permutations():
    # start by generating 4-digit primes
    digits_to_primes = dict()

    for p in prime_sieve(10000):
        # check number of digits
        if len(str(p)) < 4:
            continue
        # group primes by multisets of their digits.
        key = "".join(sorted(str(p)))
        if key in digits_to_primes:
            digits_to_primes[key].append(p)
        else:
            digits_to_primes.update({key: [p]})

    for family in digits_to_primes:
        # We don't know if some of these groups have more than 3 members so take combinations three at a time
        for comb in combinations(digits_to_primes[family], 3):

            s = list(sorted(comb))

            # check for a constant delta across the combination
            delta = s[1] - s[0]
            for i in range(1, len(s)):
                if s[i] - s[i - 1] != delta:
                    break
            else:
                yield s


def solve():
    known = set([1487, 4817, 8147])
    ps = list(count_permutations())
    for p in ps:
        if set(p) != known:
            return "".join(map(str, p))


def main():
    with TimingContext() as tc:
        s = solve()
        print(s, tc.get_duration())


if __name__ == "__main__":
    main()
