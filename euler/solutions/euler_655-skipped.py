from math import floor, ceil, log10
from itertools import product
"""
Divisible Palindromes
Problem 655

The numbers 545, 5995 and 15151 are the three smallest palindromes divisible by 109.
There are nine palindromes less than 100000 which are divisible by 109.

How many palindromes less than 10^32
are divisible by 10000019 ?
"""

"""
OEIS palindromes: https://oeis.org/A002113

'The number of palindromes with d digits is 10 if d=1, and otherwise is 9*10^(floor((d-1)/2)). - N. J. A. Sloane, Dec 06 2015'

"""
DIVISOR = 10000019


def count_palindromes(length=1):
    return 9*10**(floor(length-1)/2)


total_palindromes = sum(count_palindromes(i) for i in range(6, 32))
print('Looking for ', total_palindromes)
# quit()
c = 0
for i in range(DIVISOR, int(10**(32)), DIVISOR):
    si = str(i)
    if si == si[::-1]:
        print(si)
        c += 1
print(c)
