"""
Project Euler Problem 54
========================

In the card game poker, a hand consists of five cards and are ranked, from
lowest to highest, in the following way:

  * High Card: Highest value card.
  * One Pair: Two cards of the same value.
  * Two Pairs: Two different pairs.
  * Three of a Kind: Three cards of the same value.
  * Straight: All cards are consecutive values.
  * Flush: All cards of the same suit.
  * Full House: Three of a kind and a pair.
  * Four of a Kind: Four cards of the same value.
  * Straight Flush: All cards are consecutive values of same suit.
  * Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.

The cards are valued in the order:
2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

If two players have the same ranked hands then the rank made up of the
highest value wins; for example, a pair of eights beats a pair of fives
(see example 1 below). But if two ranks tie, for example, both players
have a pair of queens, then highest cards in each hand are compared (see
example 4 below); if the highest cards tie then the next highest cards are
compared, and so on.

Consider the following five hands dealt to two players:

        Hand   Player 1            Player 2              Winner
        1      5H 5C 6S 7S KD      2C 3S 8S 8D TD        Player 2
               Pair of Fives       Pair of Eights
        2      5D 8C 9S JS AC      2C 5C 7D 8S QH        Player 1
               Highest card Ace    Highest card Queen
        3      2D 9C AS AH AC      3D 6D 7D TD QD        Player 2
               Three Aces          Flush with Diamonds
               4D 6S 9H QH QC      3D 6D 7H QD QS
        4      Pair of Queens      Pair of Queens        Player 1
               Highest card Nine   Highest card Seven
               2H 2D 4C 4D 4S      3C 3D 3S 9S 9D
        5      Full House          Full House            Player 1
               With Three Fours    with Three Threes

The file poker.txt contains one-thousand random hands dealt to two players.
Each line of the file contains ten cards (separated by a single space): the
first five are Player 1's cards and the last five are Player 2's cards. You
can assume that all hands are valid (no invalid characters or repeated
cards), each player's hand is in no specific order, and in each hand there
is a clear winner.

How many hands does Player 1 win?
"""

from euler.solutions.utils import TimingContext
from pathlib import Path
from collections import Counter
from itertools import product, combinations

SUITS = frozenset(["C", "D", "H", "S"])
VALUES = ("2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A")
HANDS_FILE = Path(__file__).parent / "resources" / "poker.txt"


def is_card(s: str) -> bool:
    return s[-1] in SUITS and s[:-1] in VALUES


def str_to_card(s: str) -> tuple[str]:
    return (s[:-1], s[-1])


def card_value_str(s: str) -> int:
    return VALUES.index(str_to_card(s)[0])


def card_value_tuple(card: tuple[str]) -> int:
    return VALUES.index(str_to_card("".join(card))[0])


def line(s: str) -> tuple[list[str]]:
    sl = s.strip().split(" ")
    return (sl[:5], sl[5:])


def one_pair(hand: list[str]):
    """All pairs of two cards that have the same value"""

    cards = [str_to_card(s) for s in hand]
    indices = dict()
    for card in cards:
        indices.update({card[0]: indices.get(card[0], []) + [card]})
    xs = [list(combinations(v, r=2)) for v in indices.values() if len(v) >= 2]
    if xs:
        print(xs)
    # for k, v in indices.items():
    #     cs = list(combinations(v, r=2))
    #     if cs:
    #         print(["".join(t) for c in cs for t in c])
    return any(len(l) >= 2 for l in indices.values())


def two_pair(hand: list[str]):
    values = [str_to_card(s)[0] for s in hand]
    count_values = Counter(values)
    count_counts = Counter(count_values.values())
    return 2 in count_counts and count_counts[2] >= 2


def three_of_a_kind(hand: list[str]):
    """At least one value in the hand is repeated."""
    values = [str_to_card(s)[0] for s in hand]
    count_values = Counter(values)
    return 3 in count_values.values()


def straight(hand: list[str]):
    values = [str_to_card(s)[0] for s in hand]
    # values.sort(key=lambda v: VALUES.index(v))
    indices = sorted([VALUES.index(v) for v in values])
    diffs = [b - a for a, b in zip(indices, indices[1:])]
    return all(d == 1 for d in diffs)
    # print(hand, indices, diffs)


def flush(hand: list[str]):
    suits = [str_to_card(s)[1] for s in hand]


funcs: list[callable] = [one_pair, two_pair]


def solve():
    with open(HANDS_FILE) as f:
        for l in f:
            hands = line(l)
            print(hands, one_pair(hands[0]), one_pair(hands[1]))


def main():
    with TimingContext() as tc:
        s = solve()
        print(s, tc.get_duration())


if __name__ == "__main__":
    main()
