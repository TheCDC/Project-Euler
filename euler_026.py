"""
Project Euler Problem 26
========================

A unit fraction contains 1 in the numerator. The decimal representation of
the unit fractions with denominators 2 to 10 are given:

   1/2  =  0.5
   1/3  =  0.(3)
   1/4  =  0.25
   1/5  =  0.2
   1/6  =  0.1(6)
   1/7  =  0.(142857)
   1/8  =  0.125
   1/9  =  0.(1)
  1/10  =  0.1

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can
be seen that ^1/[7] has a 6-digit recurring cycle.

Find the value of d < 1000 for which ^1/[d] contains the longest recurring
cycle in its decimal fraction part.
"""


"""
2020-05-16 Conjecture: Fractions of the form a/d expressed in base b have recurring expansions when d is not a multiple of a divisor of b.

1/6 disproves this.

Conjecture 2:  Fractions of the form a/d expressed in base b have recurring expansions when d the set of prime factors of d contains a non-1 non-factor of b.
Conjecture 3:  Fractions of the form a/d expressed in base b have recurring expansions when d the set of non-1 factors of d contains a non-factor of b.
"""




from utils import isPrime
from math import floor
def does_repeat(n):
    return isPrime(n) or ((n % 2 != 0) and (n % 5 != 0))


def get_period(n):
    """Calculate period of digits of decimal expansion of 1/n"""
    remainder = 1
    i = 1
    cache = {}
    while True:
        remainder = (10*remainder) % n
        if remainder in cache:
            return i - cache[remainder]

        cache.update({remainder: i})
        i += 1


def long_division_digits(n, x):
    result = 0
    divisor = x
    dividend = n
    digit_shift = 1
    remainder = -1
    # while remainder != 0:
    for i in range(10):
        d = floor(10*dividend/divisor) % 10
        result = result*10 + d
        remainder = n*(result / (10**digit_shift))
        dividend *= 10

        digit_shift += 1
    return result


def main():
    # print(get_period(3))
    # print(get_period(7))
    # print(get_period(983))
    # print(long_division_digits(2, 7))
    fx = sorted([(i, get_period(i))
                 for i in range(1, 1000+1)], key=lambda t: t[1], reverse=True)
    print(fx[0])


if __name__ == '__main__':
    main()
