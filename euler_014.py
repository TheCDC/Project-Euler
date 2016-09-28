#!/usr/bin/env python3
import functools


@functools.lru_cache()
def collatz(n) -> int:
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1


@functools.lru_cache()
def seqlen(n) -> int:
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
    for i in range(2,1000000):
        n = seqlen(i)
        if n > longest:
            longest = n
            N = i
    # results = [(i,seqlen(i)) for i in range(2, 1000000)]
    # with open("014.txt",'w') as f:
    #     f.write('\n'.join(results))
    print(N)

if __name__ == "__main__":
    main()
