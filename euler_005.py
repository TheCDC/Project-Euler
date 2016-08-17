#!/usr/bin/env python3
from pprint import pprint

def isPrime(n):
	for i in range(2,int(n**(1/2))+1):
		if n%i == 0:
			return False
	return True

def pfactors(n):
	res = []
	if isPrime(n) or n == 4:
		return [n]
	while not isPrime(n):
		for i in range(2,int(n**(1/2))+1):
			if isPrime(i) and n%i == 0:
				res.append(i)
				n = n//i
	res.append(n)
	return res
	
def numprod(l,default=1):
	try:
		p = l[0]
		for i in l[1:]:
			p*=i
	except IndexError:
		return default
	return p

# print("hi")
# print(pfactors(75397))
for i in range(1,21):
	print(pfactors(i))
facts = [(i,pfactors(i)) for i in range(1,21)]
pprint(facts)
