"""
https://leetcode.com/problems/number-of-digit-one/description/?envType=problem-list-v2&envId=math
233. Number of Digit One
Attempted
Hard
Topics
Companies
Hint
Given an integer n, count the total number of digit 1 appearing in all non-negative integers less than or equal to n.
Example 1:
Input: n = 13
Output: 6
Example 2:
Input: n = 0
Output: 0
Constraints:
    0 <= n <= 109
"""

"""
https://oeis.org/search?q=1+1+1+1+1+1+1+1+1+2+4+5+6&language=english&go=Search
https://oeis.org/A094798
"""

from itertools import islice, count, accumulate
from math import log
from utils import directory_temp
import sys


def naive():
    s = 0
    n = 1
    while True:
        s += str(n).count("1")
        n += 1
        yield s


def upper_bound(n):
    """
    Equivalent to `sum(len(str(n)) for n in range(1,1+n))`
    Assume all digits are 1
    1,1,1,1,...,11,11,11,...111,111

    1-digit numbers (1...9) sum to 9*10**(0)
    2-digit numbers (10...99 = 10**2-10**1) sum to 2*(10**2-10**1)
    3-digit numbers (100...999 = 10**3-10**2) sum to 3*(10**3-10*21)

    upper_bound(1)=1
    upper_bound(2)=2
    upper_bound(10)=10
    upper_bound(100)=10
    """
    if n == 0:
        return 0
    exponent = int(log(n, 10))
    low = 10**exponent
    digit_lengths = list(range(1, exponent + 1))
    digit_counts = [dl * (10**dl - 10 ** (dl - 1)) for dl in digit_lengths]
    # print(digit_counts)
    sum_digit_counts = sum(digit_counts)
    remainder = (exponent + 1) * (n - low + 1)
    # print(f"{low=} {remainder=}")
    return sum_digit_counts + remainder


def guess_1(n):
    if n == 0:
        return 0
    exp = log(n, 10)
    ret = exp * 10 ** (log(n, 10) - 1) + 1
    return round(ret)


def guess_2(n):
    if n == 0:
        return 0
    digits = map(int, reversed(str(n)))
    place_values = [digit * 10**index for index, digit in enumerate(digits)]
    guesses = [guess_1(v) for v in place_values]
    sum_guesses = sum(guesses)
    return sum_guesses


class Solution:
    def countDigitOne(self, n: int) -> int:
        pass


def generate_tables():
    d = directory_temp() / "233_table_naive.txt"
    d2 = directory_temp() / "233_table_guess1_diffdiff.txt"
    print(d)
    with open(d, "w") as f:
        with open(d2, "w") as f2:
            diff = None
            for index, expected in enumerate(islice(naive(), 10**6)):
                n = index + 1
                guess = guess_2(n)
                bound = upper_bound(n)
                # guess2 = guess_2(n)
                diff_next = expected - guess
                diffdiff = diff_next - diff if diff is not None else 0
                diff = diff_next
                ratio = guess / expected
                f.write(
                    f"{n}\t{expected}\t{bound}\t{guess}\t{diff}\t{diffdiff}\t{ratio}\n"
                )
                f2.write(f"{diffdiff} ")


def ones():
    for n in count(1):
        yield str(n).count("1")


def generate_ones(n):
    p = directory_temp() / "233_ones.txt"
    with open(p, "w") as f:
        for i in islice(ones(), n):
            f.write(f"{i}\n")


def main():
    if "generate" in sys.argv:
        generate_tables()
    if "ones" in sys.argv:
        generate_ones(10000)
    # print(guess_2(1234))
    upper_bound(1234)


if __name__ == "__main__":
    main()
