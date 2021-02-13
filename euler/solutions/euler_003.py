from euler.solutions import utils

NUM = 600851475143


def solve():
    return max(utils.primeFactors(NUM))


def main():
    with utils.TimingContext() as tc:
        s = solve()
        print(s, tc.get_duration())


if __name__ == "__main__":
    main()
