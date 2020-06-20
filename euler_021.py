from utils import TimingContext
from utils import divisors
from functools import lru_cache


def d(n):
    return sum(divisors(n)[:-1])


def solve():
    known = set()
    for a in range(1, 10000):
        b = d(a)
        db = d(b)
        if db == a and b != a and not set((a, b)) & known:
            # print(a, b)
            known.add(a)
            known.add(b)

    # print(d.cache_info())
    return(sum(known))


def main():
    with TimingContext() as tc:
        s = solve()
        print(s, tc.get_duration())


if __name__ == '__main__':
    main()
