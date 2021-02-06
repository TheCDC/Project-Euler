#!/usr/bin/env python3
from timeit import default_timer
from utils import TimingContext


def solve():
    target_sum = 1000
    for c in range(1, target_sum):
        for a in range(1, target_sum-c):
            b = target_sum - a - c
            if a**2 + b**2 == c**2:
                return(a*b*c)


def main():
    with TimingContext() as tc:
        s = solve()
        print(s, tc.get_duration())


if __name__ == '__main__':
    main()
