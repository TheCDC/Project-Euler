"""
<p>The primes $3$, $7$, $109$, and $673$, are quite remarkable. By taking any two primes and concatenating them in any order the result will always be prime. For example, taking $7$ and $109$, both $7109$ and $1097$ are prime. The sum of these four primes, $792$, represents the lowest sum for a set of four primes with this property.</p>
<p>Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.</p>


"""

from itertools import combinations
from euler.solutions.utils import isPrime


def check(tup: tuple[int], debug=False):
    for a, b in combinations(tup, 2):
        if not isPrime(int(str(a) + str(b))):
            return False
        if not isPrime(int(str(b) + str(a))):
            return False
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


def clique3(edges):
    for a in edges:
        for b in edges.get(a, []):
            if not a in edges.get(b, []):
                continue
            for c in edges.get(b, []):
                if not c in edges[a]:
                    continue
                if not c in edges[b]:
                    continue
                yield a, b, c


def clique4(edges):
    memory = set()
    for a in edges:
        for b in edges.get(a, []):
            if not a in edges.get(b, []):
                continue
            for c in edges.get(b, []):
                if not c in edges.get(a, []):
                    continue
                if not c in edges.get(b, []):
                    continue
                for d in edges.get(c, []):
                    if not d in edges.get(a, []):
                        continue
                    if not d in edges.get(b, []):
                        continue
                    if not d in edges.get(c, []):
                        continue
                    fs = frozenset([a, b, c, d])
                    if fs in memory:
                        continue
                    memory.add(fs)
                    yield a, b, c, d


def clique5(edges):
    memory = set()
    for a in edges:
        for b in edges.get(a, []):
            if not a in edges.get(b, []):
                continue
            for c in edges.get(b, []):
                if not c in edges.get(a, []):
                    continue
                if not c in edges.get(b, []):
                    continue
                for d in edges.get(c, []):
                    if not d in edges.get(a, []):
                        continue
                    if not d in edges.get(b, []):
                        continue
                    if not d in edges.get(c, []):
                        continue
                    for e in edges.get(d, []):
                        if not e in edges.get(a, []):
                            continue
                        if not e in edges.get(b, []):
                            continue
                        if not e in edges.get(c, []):
                            continue
                        if not e in edges.get(d, []):
                            continue

                        fs = frozenset([a, b, c, d, e])
                        if fs in memory:
                            continue
                        memory.add(fs)
                        yield a, b, c, d, e


def v1(n=1000):
    """Generate edges between primes representing prime concatenations"""
    edges = dict()
    for i in range(n):
        for p in partitions(i):
            a, b = p
            if a == b:
                continue
            edges.update({a: edges.get(a, set()) | {b}})
            # print(i, p, a, b)
    return edges


def v2():
    """Try to find 2-cliques in edges"""
    edges = v1()
    return set(
        [
            frozenset((a, b))
            for a in edges
            for b in edges[a]
            if b in edges and a in edges[b]
        ]
    )


def v3():
    """Attempt to find 3-cliques in edges"""
    edges = v1(1000000)
    print("3-cliques")
    for c in clique3(edges):
        cc = check(c)
        if cc:
            print(cc, c)
    print("4-cliques")
    for c in clique4(edges):
        cc = check(c)
        if cc:
            print(cc, c)
    print("5-cliques")
    for c in clique5(edges):
        cc = check(c)
        if cc:
            print(cc, c)
    # for a in edges:
    #     for b in edges.get(a, []):
    #         if not a in edges.get(b, []):
    #             continue
    #         for c in edges.get(b, []):
    #             if not c in edges[a]:
    #                 continue
    #             if not c in edges[b]:
    #                 continue
    #             print(
    #                 check((a, b, c)),
    #                 a,
    #                 b,
    #                 c,
    #             )


def main():
    sanity()
    # print(v1())
    # print(v2())
    print(v3())


if __name__ == "__main__":
    main()
