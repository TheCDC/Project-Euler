from utils import TimingContext
from math import log, ceil


def nd(n):
    return ceil(log(n)/log(10))


def solve():
    i = 2
    a, b = 1, 1
    while nd(b) < 1000	:
        a, b = b, a+b
        i += 1
    return(i)


def main():
    with TimingContext() as tc:
        s = solve()
        print(s, tc.get_duration())


if __name__ == '__main__':
    main()
