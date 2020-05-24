"""
Project Euler Problem 27
========================

Euler published the remarkable quadratic formula:

                               n^2 + n + 41

It turns out that the formula will produce 40 primes for the consecutive
values n = 0 to 39. However, when n = 40, 40^2 + 40 + 41 = 40(40 + 1) + 41
is divisible by 41, and certainly when n = 41, 41^2 + 41 + 41 is clearly
divisible by 41.

Using computers, the incredible formula  n^2 - 79n + 1601 was discovered,
which produces 80 primes for the consecutive values n = 0 to 79. The
product of the coefficients, 79 and 1601, is 126479.

Considering quadratics of the form:

  n^2 + an + b, where |a| < 1000 and |b| < 1000

                              where |n| is the modulus/absolute value of n
                                               e.g. |11| = 11 and |-4| = 4

Find the product of the coefficients, a and b, for the quadratic
expression that produces the maximum number of primes for consecutive
values of n, starting with n = 0.
"""

from utils import isPrime
import timeit


def naive():
    res = []
    for a in range(-1000, 1000+1):
        for b in range(-1000, 1000+1):

            def func(x):
                return x**2 + a*x + b
            idx = 0
            item = func(0)
            while isPrime(item):
                item = func(idx)
                idx += 1
            if(idx > 39): #39 taken from data point in problem statement
                # print(a, b, a*b, idx)
                res.append((a, b, idx))
    answer = sorted(res, key=lambda t: -1, reverse=True)[0]
    return answer[0]*answer[1]


def main():
    start_time = timeit.default_timer()
    print(naive())
    elapsed = timeit.default_timer() - start_time
    print("naive", elapsed, "seconds")


if __name__ == '__main__':
    main()
