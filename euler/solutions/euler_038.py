"""
Project Euler Problem 38
========================

Take the number 192 and multiply it by each of 1, 2, and 3:

  192 * 1 = 192
  192 * 2 = 384
  192 * 3 = 576

By concatenating each product we get the 1 to 9 pandigital, 192384576. We
will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4,
and 5, giving the pandigital, 918273645, which is the concatenated product
of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as
the concatenated product of an integer with (1,2, ... , n) where n > 1?
"""

"""
NOTES
2023-01-20
Can I ("an integer") and n be derived from a pandigital?
    Given an n, can I be reasonably searched? That is, how many values of (n,I) must  be checked to check a pandigital?
        n=1
            I is 9 digits - 100000000 <= I <= 999999999
            Thankfully, n must be > 1 by fact (1)
        n=2
            I is 4 digits
            I*2 is 5 digits
            5000 <= I <= 9999
        n=3
            I is 3 digits. 100 <= I <= 999
            Is there a 2-digit number II such that II*2 is 3 digits and II*3 is 4 digits?
                The biggest 2 digit number, for which this is most likely, is 99.
                ``` calc
                                  99*2
                ```
                No, there are none.
        n=4
            (1,2,3,4)
            I=1 => 4 digits
            I=2 => 4 digits
            I=3 => 5 digits
            I=4 => 6 digits
            I=5 => 7 digits
            I=6 => 7 digits
            I=7 => 7 digits
            I=8 => 7 digits
            ...
            I=10 => 8 digits
                What's the smallest 2 digit number (10<=I<=99) II where `II*4>=100 and II*3<100`
                    `100/4=25`
                    `25*3=75`
                    lowest I=25
                Smallest I that causes `I*3` to be three digits?
                    `100/3=100/3`
                    `3*34=102`
                    `3*32=96`
                    Given n=4 the max I is 32
            I<32
        n = 5
            If I>=10 then digits(concatprod(n,I)) >= 10 which is not allowed.
            1 <= I <= 10
        n=6
            (1,2,3,4,5,6)
            I = 1?
                digits(concatprod(n,I)) = 6
            I = 2?
                digits(concatprod(n,I)) = 8
            I = 3?
                digits(concatprod(n,I)) = 9
            I >= 4?
                digits(concatprod(n,I)) >= 10
            1<=I<=3
        n=7 - no solutions
            I = 1
                digits(concatprod(n,I)) = 7
            I>=2
                digits(concatprod(n,I)) >= 10
            No solutions!
            n=8 should also have no solutions due to I=1 having n digits and I=2 having `4 + (n-4)*2 = 2*n-4` digits
                n=7 => 10
                n=8 => 12
        n=8 - no solutions
        n=9
            1<=I<=9
    Given an I, can n be reasonably searched?
        Some I's have no solutions for n. I > 987654321, for example.
        Actually, given that n>1 and that the tuple is (1,2) we must notice that the concatenation of I*1 and I*2 must me exactly 9 digits.
"""

from euler.solutions.utils import TimingContext

from itertools import combinations, permutations
from typing import List

PANDIGITAL_SET = set(range(1, 10))


def is_pandigital(n: int):
    str_n = str(n)
    set_n = set([int(d) for d in str_n])
    return len(str_n) == 9 and set_n == PANDIGITAL_SET


def get_product(n: int, i: int):
    return int("".join(map(str, (i * nn for nn in range(1, n + 1)))))


def check_n_i(n: int, i: int):
    product = get_product(n, i)
    return is_pandigital(product)


def generate_products():
    n_to_bounds_i = {
        2: (5000, 9999),
        3: (100, 999),
        4: (1, 32),
        5: (1, 10),
        6: (1, 3),
        9: (1, 9),
    }
    largest_pandigital = None
    iter_n_i = (
        (n, i)
        for n, bounds_i_inclusive in n_to_bounds_i.items()
        for i in range(bounds_i_inclusive[0], bounds_i_inclusive[1] + 1)
    )
    for index, (n, i) in enumerate(iter_n_i):
        product = (get_product(n, i), n, i, index)
        valid = is_pandigital(product[0])
        if valid:
            print(f"candidate at step={index} pandigital={product[0]} {n=} {i=}")
            largest_pandigital = (
                max(largest_pandigital, product, key=lambda l: l[0])
                if largest_pandigital
                else product
            )
    return (index + 1, largest_pandigital)


if __name__ == "__main__":
    assert check_n_i(3, 192)
    assert check_n_i(5, 9)
    with TimingContext() as tc:
        iterations, largest = generate_products()
    print(
        f"solution found after {tc.get_duration():.2f} seconds and {iterations} cases checked:\n{largest[0]} n={largest[1]} i={largest[2]}. Answer found on iteration {largest[3]}."
    )
