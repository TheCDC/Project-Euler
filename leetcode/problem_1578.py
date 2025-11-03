from itertools import groupby


class Solution:
    def minCost(self, colors: str, neededTime: list[int]) -> int:
        zipped = list(zip(colors, neededTime))
        groups = list((i[0], list(i[1])) for i in groupby(zipped, lambda t: t[0]))
        sums = [(i[0], sum(j[1] for j in i[1])) for i in groups]
        maxima = [(i[0], max(j[1] for j in i[1])) for i in groups]
        costs = [s[1] - m[1] for m, s in zip(maxima, sums)]
        return sum(costs)


def main():
    print(Solution().minCost("aabaa", [1, 2, 3, 4, 1]))


if __name__ == "__main__":
    main()
