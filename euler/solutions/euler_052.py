"""Permuted multiples
Problem 52

It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
"""
from collections import Counter


def test(n):
    digits = Counter(str(n))
    for i in range(2, 6+1):
        c = Counter(str(n*i))
        if c != digits:
            return False
    return True


def main():
    i = 0
    while True:
        i += 1
        if test(i):
            print(i)
            break


if __name__ == '__main__':
    main()
