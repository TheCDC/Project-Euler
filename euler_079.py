#!/usr/bin/env python3
class Breadcrumb():

    """Used as a marker to de-recurse the list from backtracking."""

    def __init__(self, depth):
        self.depth = depth

    def __repr__(self):
        return "Breadcrumb({})".format(self.depth)

    def __str__(self):
        return repr(self)


def test(lst, rules):
    for rule in rules:
        try:
            if lst.index(rule[1]) < lst.index(rule[0]):
                return False
        except ValueError:
            return True
    return True


def backtrack(guess, choice_pool, rules, depth=0, greedy=False):
    tails = []
    for i, c in enumerate(choice_pool):
        head = guess + [c]
        if test(head, rules):
            tail = backtrack(head,
                             choice_pool[:i] + choice_pool[i + 1:],
                             rules, depth=depth + 1, greedy=greedy)
            tails.extend([Breadcrumb(depth)] + head + tail)
            if greedy:
                break
    return tails


def interpret(l):
    """Return a list of lists from a list  delineated by Breadcrumb()'s"""
    r = []
    for i in l:
        if isinstance(i, Breadcrumb):
            r.append([])
        else:
            r[-1].extend(i)
    return r


def discard(lst, minset):
    """Return lst without items that aren't supersets of minset."""
    r = []
    for l in lst:
        if set(l) >= minset:
            r.append(l)
    return r


def main():
    with open("p079_keylog.txt") as f:
        contents = f.read().strip()
        samples = [tuple(i.strip()) for i in contents.split('\n')]
    all_digits = set(''.join(contents.split('\n')))
    choice_pool = tuple(all_digits)
    orders = []
    guess = []
    for i in samples:
        orders.append(tuple(i[:2]))
        orders.append(tuple(i[1:]))
        orders.append((i[0], i[-1]))
    sods = set(orders)
    # print(sods)
    # print(test(["1", "2", "3"], (("1", "2"),)))
    # results = backtrack([], ["1", "2", "3"], (("1", "2"), ("2", "3")))
    # pprint(interpret(results))
    # print(backtrack([], ["1"], (("1", "2"),)))
    # print(choice_pool, orders)
    results = interpret(backtrack([], choice_pool, orders))
    for i in [int(''.join(i)) for i in discard(results, all_digits)]:
        print(i, end=" ")
    print()

if __name__ == '__main__':
    main()
