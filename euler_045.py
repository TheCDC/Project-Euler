#!/usr/bin/env python3
"""Strategy
We are looking for numbers in the intersection of T, P, and H space.
We a way of testing if a given n is n those spaces.
We do that by inverting the T, P, and H functions
"""


def quadratic(a, b, c) -> float:
    sq = (b**2 - 4 * a * c)**(1 / 2)
    denom = 2 * a
    return max(((-b + sq) / denom, (-b - sq) / denom))


def tn(n) -> float:
    """nth triangle number"""
    return n * (n + 1) / 2


def nt(t) -> float:
    """n, given a triangle number"""
    return quadratic(1 / 2, 1 / 2, - t)


def pn(n) -> float:
    """nth pentagonal number"""
    return n * (3 * n - 1) / 2


def np(p) -> float:
    """n, given pentagonal number.
        If p is not a true pentagonal number
    then output will be a fraction."""
    return quadratic(3 / 2, -1 / 2, -p)


def hn(n) -> float:
    """nth hexagonal number"""
    return n * (2 * n - 1)


def nh(h) -> float:
    """n, given hexagonal number"""
    return quadratic(2, -1, -h)


def test(n) -> bool:
    """Map n to triangle space and check if that number is also found in pentagon, hexagon space."""
    a = tn(n)
    return np(a) % 1 == 0 and nh(a) % 1 == 0

# print([nt(i) for i in [1, 3, 6, 10]])
# print([np(i) for i in [1, 5, 12, 22]])
# print([nh(i) for i in [1, 6, 15, 28]])


def main():
    # sanity and correctness check
    for i in range(1,1000):
        assert (nt(tn(i))) == i
        assert (np(pn(i))) == i
        assert (nh(hn(i))) == i
    start = 40755
    i = start + 1
    while not test(i):
        i += 1
        # if i % 1000000 == 0:
        #     print("At:", i, tn(i))
    # print(i, tn(i))
    print(int(tn(i)) if tn(i) % 1 == 0 else tn(i))
if __name__ == '__main__':
    main()
