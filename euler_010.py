#!/usr/bin/env python3
sieve = [True]*(2000000)
sieve[0] = False
sieve[1] = False

mysum = 0
for n in range(2, len(sieve)):
    if not sieve[n]:
        continue
    mysum += n
    i = n*2
    for i in range(n*2,len(sieve),n):
        sieve[i] = False

print(mysum)
