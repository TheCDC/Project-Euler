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
from functools import cache
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


def upper_bound(n: int) -> int:
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


def guess_1(n: int) -> int:
    if n == 0:
        return 0
    exp = log(n, 10)
    ret = exp * 10 ** (log(n, 10) - 1) + 1
    return round(ret)


def guess_2(n: int) -> int:
    if n == 0:
        return 0
    digits = map(int, reversed(str(n)))
    place_values = [digit * 10**index for index, digit in enumerate(digits)]
    guesses = [guess_1(v) for v in place_values]
    sum_guesses = sum(guesses)
    return sum_guesses


def count_previous_runs_place(n: int, exponent: int) -> int:
    """
    The 10**0 place has runs of length 10**0 every 10**1 starting at 0
    The 10**1 place has runs of length 10**1 every 10**2 starting at 10**1
    The 10**2 place has runs of length 10**2 every 10**3 starting at 10**2


    Put another way

    Every 10**1 contributes a run of length 1 in the 10**0 place
    A RUN is a sequence of consecutive values of n each of which the digit in the
    EXPONENT place is 1
    A chunk has one run
    """
    # if n <= 10**exponent:
    #     raise ValueError(f"This function is only valid for n>=10**(exponent+1)")
    if exponent == 0:
        return n // 10
    run_length = 10**exponent
    chunk_length = 10 ** (exponent + 1)
    num_chunks = (n) // chunk_length
    count_ones_previous_runs = num_chunks * run_length
    return count_ones_previous_runs


def guess_3(n) -> int:
    """Counts the ones in ony previous ones"""
    digits = list(reversed(str(n)))
    place_counts = [
        count_previous_runs_place(n, exponent) for exponent, _ in enumerate(digits)
    ]
    sum_place_counts = sum(place_counts)
    return sum_place_counts


def count_current_run(n: int, exponent: int) -> int:
    # TODO 2024-10-11 How can you know where you are in a run for a given digit place?
    # the 10**0 place goes [1,2), [11,12), ...
    # the 10**1 place goes [10,20), [110,120), ...
    # the 10**2 place goes [100,200), [1100,1200), ...

    # MODULAR ARITHMETIC will be key in this step.
    """
    for exp=e
    look for
    """

    pass


def guess_4(n):
    """Add the ones in the current run to the lower bound set by guess_3"""
    # TODO 2024-10-11
    pass


def countDigitOne(n: int) -> int:
    # Use lru_cache decorator to memoize the results of the recursive calls
    @cache
    def dfs(position, count_ones, is_limit):
        # Base case: if no more digits to process, return the count of ones found
        if position == 0:
            return count_ones
        # Determine the upper bound for the current digit.
        # If is_limit is True, the upper bound is the current digit in the number.
        # Otherwise, it is 9 (the maximum value for a digit).
        upper_bound = digits[position] if is_limit else 9
        # Initialize the answer for this position
        ans = 0
        # Iterate over all possible digits for this position
        for digit in range(upper_bound + 1):
            # Calculate the answer recursively. Increase the count if the current digit is 1.
            # Limit flag is carried over and set to True if we reached the upper_bound.
            ans += dfs(
                position - 1,
                count_ones + (digit == 1),
                is_limit and digit == upper_bound,
            )
        return ans

    # Convert the number to a list of its digits, reversed.
    # digits = [0] * 12
    # length = 0
    # while n:
    #     digits[length + 1] = n % 10  # Store the digit
    #     n //= 10  # Move to the next digit
    #     length += 1
    digits = [0] + list(map(int, reversed(str(n))))
    # Invoke the recursive DFS function starting with the most significant digit
    return dfs(len(digits) - 1, 0, True)


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
                # guess = guess_2(n)
                guess = guess_3(n)
                bound = upper_bound(n)
                # guess2 = guess_2(n)
                diff_next = expected - guess
                diffdiff = diff_next - diff if diff is not None else 0
                diff = diff_next
                ratio = guess / expected
                f.write(f"{n}\t{expected}\t{guess}\t{diff}\t{diffdiff}\t{ratio}\n")
                f2.write(f"{diffdiff} ")


def ones():
    for n in count(1):
        yield str(n).count("1")


def ones_in_place():
    for n in count(1):
        yield "".join(c if c == "1" else " " for c in reversed(str(n)))


def generate_ones(n):
    p = directory_temp() / "233_ones.txt"
    with open(p, "w") as f:
        for i in islice(ones(), n):
            f.write(f"{i}\n")
    p = directory_temp() / "233_ones_in_place.txt"
    with open(p, "w") as f:
        for i in islice(ones_in_place(), n):
            f.write(f"{i}\n")


def test_count_previous_runs_place():
    cases = [
        (10, 0, 1),
        (100, 0, 10),
        (100, 1, 10),
        (200, 1, 20),
        (300, 1, 30),
    ]
    for n, exponent, expected in cases:
        result = count_previous_runs_place(n, exponent=exponent)
        print(
            "PASS" if result == expected else "FAIL",
            f"{n=} {exponent=} {expected=} == {result=}",
        )


def main():
    if "generate" in sys.argv:
        generate_tables()
    if "ones" in sys.argv:
        generate_ones(10**5)
    if "test" in sys.argv:
        test_count_previous_runs_place()
    test_count_previous_runs_place()
    # print(guess_2(1234))
    upper_bound(1234)
    print(countDigitOne(11))


if __name__ == "__main__":
    main()
