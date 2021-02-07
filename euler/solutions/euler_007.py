#!/usr/bin/env python3


from euler.solutions.utils import TimingContext


def isPrime(n):
    for i in range(2, int(n ** (1 / 2)) + 1):
        if n % i == 0:
            return False
    return True


def solve():
    # print([(i, isPrime(i)) for i in range(20)])
    primes = {2}
    cur = max(primes)
    while len(primes) < 10001:
        cur += 1
        if isPrime(cur):
            primes.update({cur})
    return max(primes)


def main():
    with TimingContext() as tc:
        s = solve()
        print(s, tc.get_duration())


if __name__ == "__main__":
    main()
