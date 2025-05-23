"""
Project Euler Problem 57
========================

It is possible to show that the square root of two can be expressed as an
infinite continued fraction.

            2 = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...

By expanding this for the first four iterations, we get:

1 + 1/2 = 3/2 = 1.5
1 + 1/(2 + 1/2) = 7/5 = 1.4
1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...

The next three expansions are 99/70, 239/169, and 577/408, but the eighth
expansion, 1393/985, is the first example where the number of digits in
the numerator exceeds the number of digits in the denominator.

In the first one-thousand expansions, how many fractions contain a
numerator with more digits than denominator?
"""

from fractions import Fraction
from euler.solutions.utils import TimingContext, primeFactors, numprod, reduce_fraction


class MyFraction:
    def __init__(self, numerator: int, denominator: int):
        self.numerator = numerator
        self.denominator = denominator
        pass

    def __add__(self, other: "MyFraction"):
        denom_new = self.denominator * other.denominator

        return MyFraction(
            self.numerator * other.denominator + other.numerator * self.denominator,
            denom_new,
        )

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __truediv__(self, other: "MyFraction"):
        return self * MyFraction(other.denominator, other.numerator)

    def __mul__(self, other: "MyFraction"):
        # TODO: reduce fraction using prime factors
        return MyFraction(
            self.numerator * other.numerator, self.denominator * other.denominator
        )

    def reduce(self):
        self.numerator, self.denominator = map(
            int, reduce_fraction((self.numerator, self.denominator))
        )
        return self


def v1(iterations=1):
    f = Fraction(1, 2)
    for i in range(iterations):
        f = 1 / (2 + f)
    return f


def v2():
    f = Fraction(3, 2)
    yield f.reduce()
    while True:
        f = Fraction(1, 1) + Fraction(1, 1) / (Fraction(1, 1) + f)
        yield f.reduce()


def v3():
    f = MyFraction(3, 2)
    yield f.reduce()
    while True:
        f = MyFraction(1, 1) + MyFraction(1, 1) / (MyFraction(1, 1) + f)
        yield f.reduce()


def test():
    cases = [
        (1, Fraction(3, 2)),
        (2, Fraction(7, 5)),
        (3, Fraction(17, 12)),
    ]
    for c in cases:
        iters = c[0]
        target = c[1]
        # assert list(v2)


def main():
    test()
    print((MyFraction(1, 2) + MyFraction(1, 2)).reduce())
    print((MyFraction(1, 2) / MyFraction(1, 2)).reduce())
    for i in range(1, 10):
        print(v1(i))
    with TimingContext() as tc:
        s = 0
        for frac, index in zip(v2(), range(1000)):
            print(frac, index, len(str(frac.numerator)), len(str(frac.denominator)))
            if len(str(frac.numerator)) > len(str(frac.denominator)):
                s += 1
        print(s, tc.get_duration())


if __name__ == "__main__":
    main()
