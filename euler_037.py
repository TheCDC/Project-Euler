"""
Project Euler Problem 37
========================

The number 3797 has an interesting property. Being prime itself, it is
possible to continuously remove digits from left to right, and remain
prime at each stage: 3797, 797, 97, and 7. Similarly we can work from
right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left
to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.



===========
What's the largest truncatable prime? How many digits long is it?
Maybe I can generate them.
"""
from utils import isPrime, prime_sieve

DIGITS = "1234567890"


def generate_truncatable_primes(s=""):
    if len(s) > 0 and is_truncatable(int(s)):
        yield s
    for d in DIGITS:
        sv = str(s)+d
        v = int(sv)
        if isPrime(v):
            yield from generate_truncatable_primes(sv)


def pretest(n):
    s = str(n)
    if not (isPrime(int(s[0])) and isPrime(int(s[-1]))):
        return False


def is_truncatable(n):
    s = str(n)
    if len(s) < 2:
        return False
    # left to right
    for i in range(1, len(s)):
        l = int(s[i:len(s)])
        r = int(s[0:len(s)-i])
        if not isPrime(l):
            break
        if not isPrime(r):
            break
    else:
        return True
    return False


def test():
    assert is_truncatable(3797)


def main():
    # test()
    # print(list(prime_sieve(97)))
    s = 0
    for p in generate_truncatable_primes():
        print(p)
        s += int(p)
    print("ANS:", s)


if __name__ == '__main__':
    main()
