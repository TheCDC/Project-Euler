#!/usr/bin/env python3
memory = dict()
def pascal(x,y,depth=0):
    fs = frozenset([x,y])
    if fs in memory:
        return memory[fs]
    if x == 1 or y == 1:
        ret =  1
    else:
        ret = pascal(x-1,y,depth+1) + pascal(x,y-1,depth+1)
    # print(depth*'-',x,y)
    memory.update({fs:ret})
    return ret

def main():
    print(pascal(20+1,20+1))

if __name__ == '__main__':
    main()
