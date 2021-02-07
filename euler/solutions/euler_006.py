from euler.solutions.utils import TimingContext


def solve():
    sumsq = sum([i ** 2 for i in range(1, 101)])
    sqsum = sum(list(range(1, 101))) ** 2
    # print(sumsq, sqsum, sqsum - sumsq)
    return sqsum - sumsq


def main():
    with TimingContext() as tc:
        s = solve()
        print(s, tc.get_duration())


if __name__ == "__main__":
    main()
