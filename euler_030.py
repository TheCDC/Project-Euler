#!/usr/bin/env python3
"""
Digit fifth powers
Problem 30

Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

    1634 = 14 + 64 + 34 + 44
    8208 = 84 + 24 + 04 + 84
    9474 = 94 + 44 + 74 + 44

As 1 = 14 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

"""
from utils import numDigits, nthDigit
def ds(n):
    s = 0
    for i in range(numDigits(n)):
        s += nthDigit(n,i)**5
    # print(s)
    return s
def main():
    # find an upper bound of number of digits
    nd = 1
    n = 2
    # find *a* ceiling for numbers that fit the criteria
    while n < ds(n):

        nd += 1
        n = n*10 + 9
    # lower that ceiling until the real one is found
    while n != ds(n):
        n -= 1
    # print("Upper (inclusive):",n)
    # don't include 1
    print(sum([i for i in range(2,n+1) if i == ds(i)]))
if __name__ == '__main__':
    main()