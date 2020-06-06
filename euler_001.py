#!/usr/bin/env python3
from utils import TimingContext


def solve():
    return(sum([i for i in range(1, 1000) if i % 3 == 0 or i % 5 == 0]))


def main():
    with TimingContext() as tc:
        s = solve()
        print(s, tc.get_duration())


if __name__ == '__main__':
    main()
