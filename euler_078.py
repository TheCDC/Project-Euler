"""
Coin partitions
Problem 78

Let p(n) represent the number of different ways in which n coins can be separated into piles. For example, five coins can be separated into piles in exactly seven different ways, so p(5)=7.
OOOOO
OOOO O
OOO OO
OOO O O
OO OO O
OO O O O
O O O O O

Find the least value of n for which p(n) is divisible by one million.
"""

from math import ceil


def count_distinct_piles(n, a, depth=0):
    # print(' '*depth, n, a)

    if a == 0:
        raise ValueError('Can not divide n into 0 piles!')
    if a > n:
        return 0
        raise ValueError(f'Can not have more piles than n! {a} > {n}')
    if a == 1 or n == a or a == n-1:
        # one pile
        return 1
    # only two piles
    if a == 2:
        return ceil((n - 1)/2)
    if n == a:
        # same number of piles as n
        return 1
    return 1 + count_distinct_piles(n-a, a-1, depth+1)


def partitions(n):
    return sum(count_distinct_piles(n, a) for a in range(1, n+1))


def tests():
    piles_cases = [
        {'args': (5, 1), 'result': 1},
        {'args': (5, 2), 'result': 2},
        {'args': (5, 3), 'result': 2},
        {'args': (5, 4), 'result': 1},
        {'args': (5, 5), 'result': 1},
    ]
    for case in piles_cases:
        ret = count_distinct_piles(*case['args'])
        if ret != case['result']:
            print(
                f'FAIL! args={args}, expected {case["result"]} but got {ret} ')
    # test case data from http://oeis.org/A000041
    partitions_cases = [1,
                        1,
                        2,
                        3,
                        5,
                        7,
                        11,
                        15,
                        22,
                        30,
                        42,
                        56,
                        77,
                        101,
                        135, 176, 231, 297, 385, 490, 627, 792, 1002, 1255, 1575, 1958, 2436, 3010, 3718, 4565, 5604, 6842, 8349, 10143, 12310, 14883, 17977, 21637, 26015, 31185, 37338, 44583, 53174, 63261, 75175, 89134, 105558, 124754, 147273, 173525
                        ]
    for index, expected in enumerate(partitions_cases):
        ret = partitions(index)
        if ret != expected:
            print(
                f'partitions() FAIL! args={index}, expected {expected} but got {ret} ')


tests()
print(

    count_distinct_piles(100, 3)
)
print(partitions(100))
