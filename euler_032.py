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

from math import log10
from itertools import product


def generate_exponents():
    for exp1 in range(1, 9 + 1):
        for exp2 in range(9 - exp1):
            for exp3 in range(9 - (exp1 + exp2)):
            	if exp3 == exp1 + exp2:
	                yield (exp1, exp2, exp3)


def main():
    for exps in generate_exponents():
        print(exps)


if __name__ == '__main__':
    main()