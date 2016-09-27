#!/usr/bin/env python3
import collections
import pprint
import math
from functools import lru_cache


def numprod(l, default=1):
    try:
        p = l[0]
        for i in l[1:]:
            p *= i
        return p
    except IndexError:
        return default


def isPrime(n):
    """Return whether a number is prime."""
    if n == 2:
        return True
    elif n == 1:
        return False
    try:
        for i in range(2, int(n**(1 / 2)) + 1):
            if n % i == 0:
                return False
    except Exception as e:
        print(e,n)
        raise e
    return True


def primeFactors(n):
    """Get all prime factors of a number."""
    if n == 1:
        return []
    fs = []
    while not isPrime(n) and n > 1:
        for i in range(2, int(n**(1 / 2)) + 1):
            if n % i == 0 and isPrime(i):
                fs.append(i)
                n = n // i
    if n != 1:
        fs.append(n)
    fs.sort()
    return fs


def numDivisors(n):
    """Get the number of divisors of a number."""
    if isPrime(n):
        return 2
    c = collections.Counter(primeFactors(n))
    return numprod([i + 1 for i in c.values()])


def divisors(n):
    """Get all divisors of a number."""
    l = []
    for i in range(1, int(n // 2)):
        if n % i == 0:
            l.extend([n, i / n])
    return l


def nthDigit(n, d, base=10):
    """Find digit at index n."""
    return (n % (base**(d + 1))) // (base**(d))


def numDigits(n, base=10):
    """Get the number of digits of n in base base."""
    if n == 0:
        return 1
    # if n == 1:
    #   return 1
    if base == 1:
        return n

    return math.floor(math.log(n) / math.log(base)) + 1


def numrepr(n, base):

    if base <= 10:
        d = ''
    else:
        d = ':'
    return d.join([str(nthDigit(n, i, base)) for i in range(numDigits(n, base), -1, -1)])


def fact(n):
    p = n
    while n > 1:
        n -= 1
        p *= n
    return p


def main():
    print(isPrime(3))
    print(primeFactors(57771))
    # for n in range(2, 10):
    #     for b in [2, 5, 8, 10]:
    #         print(numrepr(n, b), end=' ')
    #     print()
    # print(fact(10))
    # ns = [1, 3, 6, 10, 15, 21, 28] + list(range(1000, 2000)) + [34283340]
    # pprint.pprint([(i, len(divisors(i)), numDivisors(i), (primeFactors(i)))
    #                for i in ns])
    # pprint.pprint([ for i in ns])
    # pprint.pprint([ for i in ns])


if __name__ == '__main__':
    main()
