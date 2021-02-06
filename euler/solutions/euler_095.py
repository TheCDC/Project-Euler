"""
Project Euler Problem 95
========================

The proper divisors of a number are all the divisors excluding the number
itself. For example, the proper divisors of 28 are 1, 2, 4, 7, and 14. As
the sum of these divisors is equal to 28, we call it a perfect number.

Interestingly the sum of the proper divisors of 220 is 284 and the sum of
the proper divisors of 284 is 220, forming a chain of two numbers. For
this reason, 220 and 284 are called an amicable pair.

Perhaps less well known are longer chains. For example, starting with
12496, we form an amicable chain of five numbers:

                12496 14288 15472 14536 14264 ( 12496 ...)

Find the smallest member of the longest amicable chain with no element
exceeding one million.
"""

from utils import divisors


def proper_divisors(n):
    # import pudb;pudb.set_trace()
    ds = set(divisors(n)) - {n}
    return ds


def divisor_sum(n):
    return sum(proper_divisors(n))


def chain(n):
    found = set()
    while True:
        yield n
        dsn = set(divisors(n)) - {n}
        if n > 1000000:
            raise ValueError('Too large!')
        # print(n, len(dsn))
        n = sum(dsn)
        if n in found:
            break
        found.add(n)

# print(divisors(24))
# print(divisors(12496))
# print(sum(divisors(12496)))
# print(list(chain(12496)))
# quit()


chains = list()
longest = list()
for i in range(1, 1000000):
    # if i % 100000 == 0:
    #     print(i)
    try:
        mychain = list(chain(i))
        chains.append(mychain)
        if mychain[0] == mychain[-1]:
            # print(i,mychain)
            if len(mychain) > len(longest):
                longest = mychain
    except ValueError:
        pass

print(min(longest))
