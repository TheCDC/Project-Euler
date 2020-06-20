def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)


def solve():
    return(sum([int(i) for i in str(fact(100))]))


from utils import TimingContext

def main():
    with TimingContext() as tc:
        s = solve()
        print(s, tc.get_duration())


if __name__ == '__main__':
    main()

