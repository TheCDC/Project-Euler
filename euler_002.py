#!/usr/bin/env python3
from utils import TimingContext


def solve():
    fibs = [0, 1]
    while fibs[-1] < 4000000:
        fibs.append(fibs[-1] + fibs[-2])
    if fibs[-1] > 4000000:
        fibs.pop()
    return (sum([i for i in fibs if i % 2 == 0]))


def main():
    with TimingContext() as tc:
        s = solve()
        print(s, tc.get_duration())


if __name__ == '__main__':
    main()
