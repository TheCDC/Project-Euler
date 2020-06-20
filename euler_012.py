#!/usr/bin/env python3
"""Project Euler Problem 12
The sequence of triangle numbers is generated by adding the natural
numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 =
28. The first ten terms would be:

                 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

   1: 1
   3: 1,3
   6: 1,2,3,6
  10: 1,2,5,10
  15: 1,3,5,15
  21: 1,3,7,21
  28: 1,2,4,7,14,28

We can see that 28 is the first triangle number to have over five
divisors.

What is the value of the first triangle number to have over five hundred
divisors?
"""

from utils import TimingContext
from utils import numDivisors

# print(numDivisors(68719476735), primeFactors(68719476735))


def tris():
    i = 1
    while True:
        yield i * (i + 1) // 2
        i += 1


def solve():
    for tri in tris():
        if numDivisors(tri) > 500:
            return(tri)


def main():
    with TimingContext() as tc:
        s = solve()
        print(s, tc.get_duration())


if __name__ == '__main__':
    main()
