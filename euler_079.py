#!/usr/bin/env python3
class Breadcrumb():

    """Used as a marker to de-recurse the list result from backtracking."""

    def __init__(self, depth):
        self.depth = depth

    def __repr__(self):
        return "Breadcrumb({})".format(self.depth)

    def __str__(self):
        return repr(self)


def test(lst, rules) -> bool:
    for rule in rules:
        try:
            if lst.index(rule[1]) < lst.index(rule[0]):
                return False
        except ValueError:
            return True
    return True


def backtrack(guess, choice_pool, rules, depth=0) -> list:
    tails = []
    for i, c in enumerate(choice_pool):
        head = guess + [c]
        if test(head, rules):
            tail = backtrack(head,
                             choice_pool[:i] + choice_pool[i + 1:],
                             rules, depth=depth + 1)
            tails.extend([Breadcrumb(depth)] + head + tail)
    return tails


def interpret(l) -> list:
    """Return a list of lists from a list  delineated by Breadcrumb()'s"""
    r = []
    for i in l:
        if isinstance(i, Breadcrumb):
            r.append([])
        else:
            r[-1].extend(i)
    return r


def discard(lst, minset) -> list:
    """Return lst without items that aren't supersets of minset."""
    r = []
    for l in lst:
        if set(l) >= minset:
            r.append(l)
    return r


def get_rules(l) -> list:
    """Return a list of item ordering rules from an iterable."""
    rs = []
    for index, item in enumerate(l):
        for i in range(index):
            rs.append((l[i], item))
    return rs


def main() -> None:
    with open("p079_keylog.txt") as f:
        contents = f.read().strip()
        samples = [tuple(i.strip()) for i in contents.split('\n')]
    all_digits = set(''.join(contents.split('\n')))
    choice_pool = tuple(all_digits)
    orders = []
    for i in samples:
        orders.extend(get_rules(i))

    results = interpret(backtrack([], choice_pool, orders))
    for i in [int(''.join(i)) for i in discard(results, all_digits)]:
        print(i, end=" ")
    print()

if __name__ == '__main__':
    main()
