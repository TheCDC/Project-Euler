#!/usr/bin/env python3
from utils import isPrime
"""
Project Euler Problem 50
========================

The prime 41, can be written as the sum of six consecutive primes:

                       41 = 2 + 3 + 5 + 7 + 11 + 13

This is the longest sum of consecutive primes that adds to a prime below
one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a
prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most
consecutive primes?
"""
"""Strategy:

Find all primes below 1000000 (sieve). This will generate  N primes.

Consider sequences of length N to N-1, N-2, ... 1
    until we find a sum that is prime.

"""


def generate_by_sieve(n):
    potential_primes = list(range(n + 1))
    potential_primes[0] = False
    potential_primes[1] = False
    for i in range(2, len(potential_primes)):
        ii = i
        while ii < len(potential_primes):
            ii += i
            if ii < len(potential_primes):
                potential_primes[ii] = False
    for p, flag in enumerate(potential_primes):
        if flag:
            yield p


def main():
    debug = True
    N = 1000000
    if debug:
        print('Generating primes')
    relevant_primes = list(generate_by_sieve(N))
    # print(list(generate_by_sieve(1000000)))
    if debug:
        print('Pruning primes')
    c = 0
    while relevant_primes[-1] + relevant_primes[-2] > 1000000:
        relevant_primes.pop()
        c += 1

    if debug:
        print('Pruned', c)
        print('Generating intermediate sums')
    intermediate_sums = [
        sum(relevant_primes[:i]) for i in range(len(relevant_primes))
    ]

    print('Pruned', c, 'primes')
    if debug:
        print('Searching for matching sequence')
    for seqlen in range(N, 1, -1):
        if debug:
            if seqlen % 10000 == 0:
                print(seqlen)
        for offset in range(N - seqlen):
            try:
                s = intermediate_sums[offset
                                      + seqlen] - intermediate_sums[offset]
            except IndexError:
                break
            if s < 1000000:
                if isPrime(s):
                    print(s)
                    quit()


if __name__ == '__main__':
    main()
