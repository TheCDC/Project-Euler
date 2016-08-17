#!/usr/bin/env python3
"""
Problem 18: Maximum path sum I

By starting at the top of the triangle below and moving to adjacent
numbers on the row below, the maximum total from top to bottom is 23.

                                    3
                                   7 4
                                  2 4 6
                                 8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

                                    75
                                  95 64
                                 17 47 82
                               18 35 87 10
                              20 04 82 47 65
                            19 01 23 75 03 34
                           88 02 77 73 07 63 67
                         99 65 04 28 06 16 70 92
                        41 41 26 56 83 40 80 70 33
                      41 48 72 33 47 32 37 16 94 29
                     53 71 44 65 25 43 91 52 97 51 14
                   70 11 33 28 77 73 17 78 39 68 17 57
                  91 71 52 38 17 14 91 43 58 50 27 29 48
                63 66 04 68 89 53 67 30 73 16 69 87 40 31
               04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

NOTE: As there are only 16384 routes, it is possible to solve this problem
   by trying every route. However, Problem 67, is the same challenge with
a triangle containing one-hundred rows; it cannot be solved by brute
force, and requires a clever method! ;o)

"""

"""
Perhaps begin by collapsing the entire triangle into the second
(length-2) row. This would create a score. Choose the options with the highest score.
Repeat by collapsing all remaining options into the next row and so on.
"""


import functools
from math import ceil
from pprint import pprint
triangle = """                      75
                                  95 64
                                 17 47 82
                               18 35 87 10
                              20 04 82 47 65
                            19 01 23 75 03 34
                           88 02 77 73 07 63 67
                         99 65 04 28 06 16 70 92
                        41 41 26 56 83 40 80 70 33
                      41 48 72 33 47 32 37 16 94 29
                     53 71 44 65 25 43 91 52 97 51 14
                   70 11 33 28 77 73 17 78 39 68 17 57
                  91 71 52 38 17 14 91 43 58 50 27 29 48
                63 66 04 68 89 53 67 30 73 16 69 87 40 31
               04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""
triangle = [[int(j) for j in i.strip().split()] for i in triangle.split('\n')]
st = sum([sum(i) for i in triangle])
print("SUMS:", st, st - sum(triangle[-1]))
# print(triangle)


def getpos(tri, l, r):
    # print('l', l, 'r', r)
    try:
        # print(ceil(len(tri[l + r]) / 2) + r - l)
        x = l + r
        y = r
        # print(x, y)
        return tri[x][y]
    except IndexError:
        raise ValueError


def setpos(tri, l, r, val):
    try:
        tri[l + r][r - l] = val
    except IndexError:
        raise ValueError


def goRight(tri, l, r):
    s = 0
    try:
        s += getpos(tri, l, r)
        s += goRight(tri, l, r + 1)
    except ValueError:
        pass
    return s


def goLeft(tri, l, r):
    s = 0
    try:
        s += getpos(tri, l + 1, r)
        s += goLeft(tri, l + 1, r)
    except ValueError:
        pass
    return s
# @functools.lru_cache(maxsize=128)


def sumBelow(tri, l, r, hist=None):
    s = 0
    s += getpos(tri, l, r)
    try:
        s += sumBelow(tri, l + 1, r)
    except:
        pass
    try:
        s += goRight(tri, l, r + 1)
    except:
        pass
    return s


def main():
    # print(getpos(triangle, 0, 0))
    # print(getpos(triangle, 0, 14))
    # print(sumBelow(triangle, 0, 0))
    for i in range(8):
        print(getpos(triangle, i, i))
        # print(getpos(triangle, i, 0), getpos(triangle, 0, i))
    print(getpos(triangle, 7, 7))
    # print(getpos(triangle, i, 0))
    # print()
    decisionTree = triangle[:]
    for l in range(len(triangle)):
        for r in range( len(triangle) - l ):
            # print(l+r)
            # print(l, r, l+r)
            setpos(decisionTree, l, r, sumBelow(triangle, l, r))
    print("DTree:", decisionTree)
    # print(goLeft(triangle, 0, 0))
    # print(goRight(triangle, 0, 0))
    # now make each position in the decisiontree
    # equal to the sum of the triangle of which it
    # is the apex

if __name__ == '__main__':
    main()
