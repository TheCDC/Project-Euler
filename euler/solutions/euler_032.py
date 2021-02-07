"""
Project Euler Problem 32
========================

We shall say that an n-digit number is pandigital if it makes use of all
the digits 1 to n exactly once; for example, the 5-digit number, 15234,
is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 * 186 = 7254, containing
multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product
identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to
only include it once in your sum.
"""

from itertools import permutations
import sys


def generate_exponents():
    digits = 9
    ds = [1, 2, 3, 4]
    for exp1 in ds:
        for exp2 in ds:
            exp3 = digits - (exp1 + exp2)
            if sum([exp1,exp2,exp3]) == digits:
                yield (exp1, exp2, exp3)
    return 
    for exp1 in range(1, digits):
        for exp2 in range(1, digits - exp1):
            exp3 = digits - (exp1 + exp2)
            if exp1 + exp2 - 1 > exp3:
                break
            if exp1 + exp2 < exp3:
                continue
            if abs((exp1 + exp2) - exp3) > 1:
                break

            # if exp3 <= 0:
            #     break
            # if exp1 + exp2 - 1 > exp3:
            #     break

            yield (exp1, exp2, exp3)


def generate_pandigitals(start=1, stop=10):
    for i in range(start, stop):
        yield from permutations(set(range(1, i + 1)))


def main():
    if 'debug' in sys.argv:
        for exps in generate_exponents():
            print(exps)
    found = set()
    for pan in generate_pandigitals(start=9, stop=10):
        for exps in generate_exponents():
            a = int(''.join(map(str, pan[:exps[0]])))
            b = int(''.join(map(str, pan[exps[0]:exps[0] + exps[1]])))
            c = int(''.join(map(str, pan[exps[0] + exps[1]:])))
            if a * b == c:
                if 'debug' in sys.argv:
                    print(a, b, c)
                found.add(c)
    if 'debug' in sys.argv:
        print('Done solving')

    # discount duplicates
    print(sum(found))


if __name__ == '__main__':
    main()
