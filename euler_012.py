#!/usr/bin/env python3
from utils import numDivisors, primeFactors, divisors
from pprint import pprint
# print(numDivisors(68719476735), primeFactors(68719476735))
n = 1 
numdivs = numDivisors(n)
most = numdivs
tri = sum(range(n+1))
tris = [n]
try:
    while numdivs < 501:
        if numdivs > most:
            most = numdivs
            print(n,tri, numdivs)
        n += 1
        tri = sum(range(n+1))
        tris.append(tri)
        numdivs = numDivisors(tri)
except KeyboardInterrupt:
    print("Stopped at:", n, numdivs)
nd = divisors(tri)
print(n,tri, numDivisors(tri), nd, len(nd))
# pprint([(i,numDivisors(i)) for i in tris[-10:]])
