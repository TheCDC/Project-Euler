#!/usr/bin/env python3
import functools


def collatz(n):
    if n % 2 == 0:
        return n / 2
    else:
        return 3 * n + 1


@functools.lru_cache()
def seqlen(n):
    l = 0
    while n != 1:
        n = collatz(n)
        l += 1
    l += 1
    return l


def main():
        # print(seqlen(13))
        # print(seqlen(100))
        # print(seqlen(10000))

    longest = 0
    N = 0
    results = [(i,seqlen(i) for i in range(2, 1000000)]:
    with open("014.txt",'w') as f:
        f.write('\n'.join(results))
    print(N)

if __name__ == "__main__":
    main()
