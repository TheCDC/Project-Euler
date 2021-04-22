from math import floor, ceil
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


def count_palindromes(length=1):
    return 9*10**(floor(length-1)/2)


def palindromes(length=1):
    for p in product(*[range(10) for _ in range(ceil(length/2))]):
        if p[0] == 0:
            continue
        if length > 1:
            if length % 2 == 0:
                yield int(''.join(map(str, p + p[::-1])))
            yield int(''.join(map(str, p[:-1] + (p[-1],) + p[:-1][::-1])))


print(list(palindromes(4)))
total_palindromes = sum(count_palindromes(i) for i in range(6, 32))
print('Looking for ', total_palindromes)
# quit()

c = 0
for length in range(13, 32):
    print('length:', length, f'found {c} so far')
    for p in palindromes(length):
        if p % 10000019 == 0 and p > 0:
            c += 1
            print('Found:', p)
print(c)
