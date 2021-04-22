"""
Project Euler Problem 33


The fraction 49/98 is a curious fraction, as an inexperienced
mathematician in attempting to simplify it may incorrectly believe that
49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less
than one in value, and containing two digits in the numerator and
denominator.

If the product of these four fractions is given in its lowest common
terms, find the value of the denominator.
"""
from typing import List, Set, Generator, Tuple
from euler.solutions.utils import reduce_fraction  # hand-written
from timeit import default_timer


def find_all_examples() -> Generator[Tuple[int, int], None, None]:
    for f in generate_fractions():
        for c in cancel(f):
            if c[0] / c[1] == f[0] / f[1]:
                # print(f, c)
                yield f, c


def cancel(f: List[int]):
    for d in shared_digits(f):
        cancelled_fraction = (delete_digit(f[0], d), delete_digit(f[1], d))
        if cancelled_fraction[1] > 0:
            yield cancelled_fraction


def generate_fractions() -> Generator[Tuple[int, int], None, None]:
    for i in range(10, 99 + 1):
        for j in range(i + 1, 99 + 1):
            f = (i, j)
            if can_cancel(f) and not is_trivial(f):
                yield f


def is_trivial(f: Tuple[int, int]) -> bool:
    return f[0] % 10 == 0 and f[1] % 10 == 0


def can_cancel(f: Tuple[int, int]) -> bool:
    return len(shared_digits(f)) > 0


def shared_digits(f: Tuple[int, int]) -> Set[str]:
    numerator = f[0]
    denominator = f[1]
    return set(str(numerator)) & set(str(denominator))


def delete_digit(n: int, d: int) -> int:
    ds = list(str(n))
    ds.remove(str(d))
    return int("".join(ds))


def main():
    start = default_timer()
    p = [1, 1]
    for f, c in find_all_examples():
        # print(f, c)
        p[0] *= c[0]
        p[1] *= c[1]
    reduced = reduce_fraction(p)
    print("/".join(map(str, reduced)), default_timer() - start, "seconds")


if __name__ == "__main__":
    main()
