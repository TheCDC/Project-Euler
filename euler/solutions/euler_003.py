from euler.solutions.utils import TimingContext

NUM = 600851475143


def solve():
    return max(utils.primeFactors(NUM))


def main():
    with TimingContext() as tc:
        s = solve()
        print(s, tc.get_duration())


if __name__ == "__main__":
    main()
