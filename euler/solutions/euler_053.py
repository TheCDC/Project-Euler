"""Combinatoric selections
Problem 53

There are exactly ten ways of selecting three from five, 12345:

123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

In combinatorics, we use the notation, 5C3 = 10.

In general,
nCr = 	
n!
r!(n−r)!
	,where r ≤ n, n! = n×(n−1)×...×3×2×1, and 0! = 1.

It is not until n = 23, that a value exceeds one-million: 23C10 = 1144066.

How many, not necessarily distinct, values of  nCr, for 1 ≤ n ≤ 100, are greater than one-million?
"""
from functools import lru_cache


@lru_cache(maxsize=1000000)
def factorial(n):
    if n <= 1:
        return 1
    return n*factorial(n-1)


def ncr(n, r):
    return factorial(n)/(factorial(r)*factorial(n-r))


def main():

    c = 0
    for n in range(1, 100+1):
        flag = False
        for r in range(n, 0, -1):
            res = ncr(n, r)
            if res > 1000000:
                c += 1
                flag = True
            if res < 1000000 and flag:
                break
    print(c)


if __name__ == '__main__':
    main()
