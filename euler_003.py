NUM = 600851475143


def isPrime(n):
    for i in range(2, int(n**(1 / 2)) + 1):
        if n % i == 0:
            return False
    return True
print(isPrime(NUM))
N = NUM
while not isPrime(N):
    for i in range(2, int(NUM**(1 / 2)) + 1):
        if isPrime(i) and N % i == 0:
            N = N // i
            print(N)
print(N)

big = 0	
for i in range(2, int(NUM**(1 / 2)) + 1):
    if isPrime(i) and NUM % i == 0:
        big = i

print(big)

# print(primes[-10:-1:-1])
