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

q = {1: [[1]]}


def decompose(n):
    try:
        return q[n]
    except:
        pass

    result = [[n]]

    for i in range(1, n):
        a = n-i
        R = decompose(i)
        for r in R:
            if r[0] <= a:
                result.append([a] + r)

    q[n] = result
    return result


def count_distinct_piles(n):
    return len(decompose(n))


def tests():
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
        ret = count_distinct_piles(index)
        if ret != expected:
            print(
                f'partitions() FAIL! args={index}, expected {expected} but got {ret} ')
        else:
            print(
                f'partitions() SUCCESS! args={index}, got {ret} ')


tests()
for i in range(49, 100):
    r = count_distinct_piles(i)

    print(i,
          r, r % 1000000 == 0
          )
print(partitions(100))
