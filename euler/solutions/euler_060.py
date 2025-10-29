"""
<p>The primes $3$, $7$, $109$, and $673$, are quite remarkable. By taking any two primes and concatenating them in any order the result will always be prime. For example, taking $7$ and $109$, both $7109$ and $1097$ are prime. The sum of these four primes, $792$, represents the lowest sum for a set of four primes with this property.</p>
<p>Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.</p>


"""

from itertools import combinations
from euler.solutions.utils import isPrime, TimingContext, prime_sieve


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
    if not isPrime(i):
        return
    si = str(i)
    for i in range(len(si)):
        sa = si[:i]
        sb = si[i:]
        if len(sa) == 0 or len(sb) == 0:
            continue
        ia = int(sa)
        ib = int(sb)
        if (str(ia) == sa and str(ib) == sb) and (isPrime(ia) and isPrime(ib)):
            if isPrime(int(sa + sb)):
                yield ia, ib
            if isPrime(int(sb + sa)):
                yield ib, ia


def get_edges(n: int):
    for p in partitions(n):
        a, b = p
        if a == b:
            continue
        yield a, b


def edges_new(n, previous: dict[int, set[int]] = None):
    previous = previous if previous is not None else dict()
    for a, b in get_edges(n):
        if not b in previous.get(a, set()):
            yield a, b


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


def clique5(edges: dict, target: int = None):
    """TODO: look only for cliques containing the latest primes added to the edges."""
    memory = set()
    for a in [target] if target else edges:
        for b in edges.get(a, []):
            if not a in edges.get(b, []):
                continue
            for c in edges.get(b, []):
                if not c in edges.get(a, []):
                    continue
                if not c in edges.get(b, []):
                    continue
                if a not in edges.get(c, []) or b not in edges.get(c, []):
                    continue
                for d in edges.get(c, []):
                    if not d in edges.get(a, []):
                        continue
                    if not d in edges.get(b, []):
                        continue
                    if not d in edges.get(c, []):
                        continue
                    if (
                        a not in edges.get(d, [])
                        or b not in edges.get(d, [])
                        or c not in edges.get(d, [])
                    ):
                        continue
                    # print("4-clique", a, b, c, d)
                    for e in edges.get(d, []):
                        if not e in edges.get(a, []):
                            continue
                        if not e in edges.get(b, []):
                            continue
                        if not e in edges.get(c, []):
                            continue
                        if not e in edges.get(d, []):
                            continue
                        if (
                            a not in edges.get(e, [])
                            or b not in edges.get(e, [])
                            or c not in edges.get(e, [])
                            or d not in edges.get(e, [])
                        ):
                            continue
                        fs = frozenset([a, b, c, d, e])
                        if fs in memory:
                            continue
                        memory.add(fs)
                        yield a, b, c, d, e


def v1(n=1000, on_update: callable = None):
    """Generate edges between primes representing prime concatenations"""
    edges = dict()
    for i in range(n):
        for p in partitions(i):
            a, b = p
            if a == b:
                continue
            edges.update({a: edges.get(a, set()) | {b}})
            # print(i, p, a, b)
            if on_update:
                print("call update on", a)
                on_update(edges, a)
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


def v4():
    """
    Iterate over ints
        for each, generate partitions and edges from partitions
    """
    print(list(prime_sieve(32)))
    memory = set()
    smallest = None
    with TimingContext() as tc:
        edges = dict()
        for index, n in enumerate(prime_sieve(1000000)):
            if index % 10000 == 0:
                print("progress", index, n, tc.get_duration())
            for p in partitions(n):
                a, b = p
                if a == b:
                    continue
                edges.update({a: edges.get(a, set()) | {b}})
                # print(i, p, a, b)
                cliques = list(clique5(edges, a))
                if cliques:
                    # print("5-CLIQUE FOUND!", cliques)
                    for c in cliques:
                        fsc = frozenset(sorted(c))
                        if fsc not in memory:
                            memory.add(fsc)
                            if smallest is None or sum(fsc) < smallest:
                                smallest = sum(fsc)
                                print(smallest, check(fsc), *sorted(fsc))
                            yield fsc


def v5():
    memory: dict[int, set[int]] = dict()
    for i in range(2000000):
        en = edges_new(i, memory)
        for a, b in en:
            memory.update({a: memory.get(a, set()) | set([b])})
            cs = list(clique5(memory, a))
            if cs:
                print("5-cliques", cs)
    print("primes", len(memory))


def main():
    sanity()
    # print(v1())
    # print(v2())
    # print(v3())
    # print(list(v4()))
    v5()


if __name__ == "__main__":
    main()
