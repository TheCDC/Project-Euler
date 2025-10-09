"""
<p>The primes $3$, $7$, $109$, and $673$, are quite remarkable. By taking any two primes and concatenating them in any order the result will always be prime. For example, taking $7$ and $109$, both $7109$ and $1097$ are prime. The sum of these four primes, $792$, represents the lowest sum for a set of four primes with this property.</p>
<p>Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.</p>


"""

from itertools import combinations
from euler.solutions.utils import isPrime


def check(tup: tuple[int], debug=False):
    for a, b in combinations(tup, 2):
        if not isPrime(int(str(a) + str(b))):
            continue
        if not isPrime(int(str(b) + str(a))):
            continue
        if debug:
            print(a, b)
    return True


def partitions(i: int):
    si = str(i)
    for i in range(len(si)):
        a = si[:i]
        b = si[i:]
        if len(a) == 0 or len(b) == 0:
            continue
        ia = int(a)
        ib = int(b)
        if isPrime(ia) and isPrime(ib):
            if isPrime(int(a + b)):
                yield ia, ib
            if isPrime(int(b + a)):
                yield ib, ia


def sanity():
    print("Sanity check start")
    print(check((3, 7, 109, 673), debug=True))
    print("Sanity check passed")
    # for a, b in combinations((3, 7, 109, 673), 2):
    #     iab = int(str(a) + str(b))
    #     print(list(partitions(iab)))
    print(list(partitions(23)))


def v1(n=1000):
    """Generate edges between primes representing prime concatenations"""
    edges = dict()
    for i in range(n):
        for p in partitions(i):
            a, b = p
            if a == b:
                continue
            edges.update({a: edges.get(a, set()) | {b}})
            # edges.update({b: edges.get(b, set()) | {a}})
            # print(i, p, a, b)
    return edges


def v2():
    pass


def main():
    sanity()
    print(v1())


if __name__ == "__main__":
    main()
