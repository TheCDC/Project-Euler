#!/usr/bin/env python3
from utils import TimingContext


def solve():
    sieve = [True]*(2000000)
    sieve[0] = False
    sieve[1] = False

    mysum = 0
    for n in range(2, len(sieve)):
        if not sieve[n]:
            continue
        mysum += n
        i = n*2
        for i in range(n*2, len(sieve), n):
            sieve[i] = False

    return(mysum)


def main():
    with TimingContext() as tc:
        s = solve()
        print(s, tc.get_duration())


if __name__ == '__main__':
    main()
