#!/usr/bin/env python3
from euler.solutions.utils import TimingContext


def solve_naive():
    return sum([i for i in range(1, 1000) if i % 3 == 0 or i % 5 == 0])


def sum_integers_one_to_n(n: int) -> int:
    if n % 2 == 0:
        return (n + 1) * n // 2
    return (n + 2) * (n // 2) + 1


def solve():
    return (
        sum_integers_one_to_n(999 // 3) * 3
        + sum_integers_one_to_n(999 // 5) * 5
        - sum_integers_one_to_n(999 // 15) * 15
    )


def main():
    with TimingContext() as tc:
        s = solve()
        print(s, tc.get_duration())


if __name__ == "__main__":
    main()
