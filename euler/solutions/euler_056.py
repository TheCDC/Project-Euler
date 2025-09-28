"""
Project Euler Problem 56
========================

A googol (10^100) is a massive number: one followed by one-hundred zeros;
100^100 is almost unimaginably large: one followed by two-hundred zeros.
Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, a^b, where a, b < 100, what is
the maximum digital sum?
"""

from euler.solutions.utils import TimingContext


def solve(show=False):
    m = 0
    for a in range(1, 101):
        for b in range(1, 101):
            ss = sum(map(int, str(a**b)))
            if ss > m and show:
                print(ss, a, b)
            m = max(m, ss)
    return m


def main():
    with TimingContext() as tc:
        s = solve()
        print(s, tc.get_duration())


if __name__ == "__main__":
    main()
