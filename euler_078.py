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
def partitions(n,a):

    if a == 0:
        raise ValueError('Can not divide n into 0 piles!')
    if a > n:
        raise ValueError('Can not have more piles than n!')
    if a == 1:
        # one pile
        return 1
    # only two piles 
    if a == 2:
        return ceil((n -1)/2)
    if n == a:
        # same number of piles as n
        return 1
    s = 0
    for i in range(1,n):
        try:
            s +=  partitions(n-i,a-1)
        except ValueError:
            pass
    return s
print(

partitions(5, 3)
)