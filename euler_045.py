def tn(n):
    return n*(n+1)/2


def nt(t):
    sq = (1 - 4*(-2*t))**(1/2)
    return max((-1/2 + sq/2, -1/2 - sq/2))


def pn(n):
    return n*(3*n-1)/2


def np(p):
    sq = (1 - 4*(3*(-2*p)))**(1/2)
    return max((1/6 + sq/6, 1/6 - sq/6))


def hn(n):
    return n*(2*n-1)


def nh(h):
    sq = (1-4*2*(-h))**(1/2)
    return max((1/4 + sq/4, 1/4 - sq/4))


def test(n):
    a = tn(n)
    return np(a) % 1 == 0 and nh(a) % 1 == 0

# print([nt(i) for i in [1, 3, 6, 10]])
# print([np(i) for i in [1, 5, 12, 22]])
# print([nh(i) for i in [1, 6, 15, 28]])


def main():
    start = 40755
    i = start + 1
    while not test(i):
        i += 1
        if i % 1000000 == 0:
            print("At:", i, tn(i))
    # print(i, tn(i))
    print(i)
if __name__ == '__main__':
    main()
