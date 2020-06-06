#!/usr/bin/env python3
from timeit import default_timer
from utils import TimingContext


def solve():
    SUM = 1000
    for c in range(1, SUM):
        for a in range(1, SUM-c):
            b = SUM - a - c
            if a**2 + b**2 == c**2:
                return(a*b*c)


def main():
    with TimingContext() as tc:
        s = solve()
        print(s, tc.get_duration())


if __name__ == '__main__':
    main()
