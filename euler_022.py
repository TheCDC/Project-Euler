from utils import TimingContext
with open("p022_names.txt") as f:
    contents = f.read()
names = sorted([i.strip('"') for i in contents.split(',')])


def score(s):
    return sum([ord(i) - 65 + 1 for i in s])

# print(names[:10])


def solve():
    return(sum(score(item)*(index+1) for index, item in enumerate(names)))


def main():
    with TimingContext() as tc:
        s = solve()
        print(s, tc.get_duration())


if __name__ == '__main__':
    main()
