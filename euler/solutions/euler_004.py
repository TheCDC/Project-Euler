from euler.solutions.utils import TimingContext


def solve():
    big = 0

    for first in range(1000, 99, -1):
        for second in range(1000, 99, -1):
            product = first * second
            if str(product) == str(product)[::-1]:
                if product > big:
                    print(product, first, second)
                    big = product
                    # print(big)

    return big
    # print(max([i for i in range(100,100**2) if str(i) == str(i)[::-1]]))


def main():
    with TimingContext() as tc:
        s = solve()
        print(s, tc.get_duration())


if __name__ == "__main__":
    main()
