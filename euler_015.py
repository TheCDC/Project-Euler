#!/usr/bin/env python3
from functools import lru_cache


memory = dict()
lru_cache(maxsize=100000)
def pascal(x,y):
    fs = frozenset([x,y])
    if fs in memory:
        return memory[fs]
    if x == 1 or y == 1:
        return 1
    ret = pascal(x-1,y) + pascal(x,y-1)
    memory.update({fs:ret})
    return ret

def main():

    # print([numPaths((i,i)) for i in range(15)])
    print(pascal(20+1,20+1))

if __name__ == '__main__':
    main()
