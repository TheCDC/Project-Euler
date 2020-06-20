#!/usr/bin/env python3
from utils import TimingContext


def solve():
    s = str(2**1000)
    n = sum([int(i) for i in s])
    return(n)


def main():
    with TimingContext() as tc:
        s = solve()
        print(s, tc.get_duration())


if __name__ == '__main__':
    main()
