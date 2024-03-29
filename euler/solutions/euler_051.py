from .utils import prime_sieve, isPrime
from itertools import groupby, product
import sys

DIGITS = tuple(range(0, 10))
LIMIT_UPPER = 100000


def num_different_digits(a, b):
    if len(str(a)) != len(str(b)):
        raise ValueError
    return sum([ac != bc for ac, bc in zip(str(a), str(b))])


def digit_length(n):
    return len(str(n))


def solve_with_limit(limit_upper, family_size_target=8):
    ps = list(prime_sieve(limit_upper))
    family_biggest = set()
    for p in ps:
        sp = str(p)
        dl = digit_length(p)
        for binary_mask in product([True, False], repeat=dl):
            family = set()
            if sum(binary_mask) == 0:
                continue
            for digit in DIGITS:
                neighbor_potential = int(
                    "".join(
                        map(
                            str,
                            (
                                digit if digit_is_masked else prime_digit
                                for digit_is_masked, prime_digit in zip(binary_mask, sp)
                            ),
                        )
                    )
                )
                if (
                    isPrime(neighbor_potential)
                    and digit_length(neighbor_potential) == dl
                ):
                    family.add(neighbor_potential)
            if len(family) == family_size_target:
                return family
            if len(family) > len(family_biggest):
                family_biggest = family
                print(list(sorted(family_biggest)), file=sys.stderr)
    sfb = list(sorted(family_biggest))
    print(len(sfb), sfb, list(isPrime(p) for p in sfb), file=sys.stderr)
    return sfb


def main():
    limit = 10000
    s = []
    while len(s) < 8:
        if len(s) > 0:
            print(
                "Upper limit too low, found a family of only size",
                len(s),
                file=sys.stderr,
            )
        limit *= 2
        print("Solving with limit of", limit, file=sys.stderr)
        s = solve_with_limit(limit)
    print(list(sorted(s)), file=sys.stderr)
    print(min(s))


if __name__ == "__main__":
    main()
