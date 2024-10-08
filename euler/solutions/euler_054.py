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

from collections import Counter
from euler.solutions.utils import TimingContext
from itertools import combinations
from pathlib import Path
from typing import Callable

SUITS = frozenset(["C", "D", "H", "S"])
VALUES = ("2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A")
HANDS_FILE = Path(__file__).parent / "resources" / "poker.txt"
HANDS_FILE_TEST = Path(__file__).parent / "resources" / "poker-test.txt"
HANDS_FILE_TEST_2 = Path(__file__).parent / "resources" / "poker-test2.txt"


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


def one_pair(hand: list[str]) -> int:
    """The highest valued pair, if any"""

    cards = [str_to_card(s) for s in hand]
    indices = dict()
    for card in cards:
        indices.update({card[0]: indices.get(card[0], []) + [card]})
    matches = [k for k, v in indices.items() if len(v) == 2]
    if not matches:
        return 0
    return max(VALUES.index(s) for s in matches) + 1


def two_pair(hand: list[str]) -> int:
    """At least one value in the hand appears twice"""

    values = [str_to_card(s)[0] for s in hand]
    count_values = Counter(values)
    count_counts = Counter(count_values.values())
    if not (2 in count_counts and count_counts[2] >= 2):
        return 0
    return max(VALUES.index(k) for k, v in count_values.items() if v >= 2) + 1


def three_of_a_kind(hand: list[str]) -> int:
    """At least one value in the hand appears three times"""
    values = [str_to_card(s)[0] for s in hand]
    count_values = Counter(values)
    if not 3 in count_values.values():
        return 0
    return max(VALUES.index(k) for k, v in count_values.items() if v == 3) + 1


def straight(hand: list[str]) -> int:
    cards = [str_to_card(s) for s in hand]
    # values.sort(key=lambda v: VALUES.index(v))
    indices = sorted(card_value_tuple(c) for c in cards)
    diffs = [b - a for a, b in zip(indices, indices[1:])]
    if not all(d == 1 for d in diffs):
        return 0
    return max(VALUES.index(c[0]) for c in cards) + 1
    # print(hand, indices, diffs)


def flush(hand: list[str]) -> int:
    """All cards in the hand are the same suit."""
    cards = [str_to_card(s) for s in hand]
    suits = [card[1] for card in cards]
    n = len(set(suits))
    if not n == 1:
        return 0
    return max(VALUES.index(c[0]) for c in cards) + 1


def full_house(hand: list[str]) -> int:
    cards = [str_to_card(s) for s in hand]
    values = [str_to_card(s)[0] for s in hand]
    count_values = Counter(values)
    counts_distinct = set(count_values.values())
    if not counts_distinct == set([2, 3]):
        return 0
    return [VALUES.index(k) for k, v in count_values.items() if v == 3][0] + 1
    # return max(VALUES.index(c[0]) for c in cards) + 1


def four_of_a_kind(hand: list[str]) -> int:
    values = [str_to_card(s)[0] for s in hand]
    count_values = Counter(values)
    vs = count_values.values()
    if not 4 in vs:
        return 0
    return max(VALUES.index(k) for k, v in count_values.items() if v == 4) + 1


def straight_flush(hand: list[str]) -> int:
    cards = [str_to_card(s) for s in hand]
    counts_suits = Counter(c[1] for c in cards)
    if not (
        len(counts_suits.keys()) == 1 and 5 in counts_suits.values() and straight(hand)
    ):
        return 0
    return max(VALUES.index(c[0]) for c in cards)


def royal_flush(hand: list[str]) -> int:
    values = [str_to_card(s)[0] for s in hand]
    if not (flush(hand) and set(values) == set(VALUES[-5:])):
        return 0
    return max(VALUES.index(v) for v in values) + 1


def high_card(hand: list[str]) -> int:
    values = [str_to_card(s)[0] for s in hand]
    # return sorted(values, key=lambda x: VALUES.index(x))
    return max(VALUES.index(v) for v in values) + 1


funcs_rank: list[Callable] = [
    one_pair,
    two_pair,
    three_of_a_kind,
    straight,
    flush,
    full_house,
    four_of_a_kind,
    straight_flush,
    royal_flush,
]


def rank_hand(hand: list[str]):
    for index, f in enumerate(funcs_rank):
        rank_value = f(hand)
        if rank_value:
            yield index, rank_value


def winner(hand_a: list[str], hand_b: list[str], index: int = None) -> int:
    ranks_hand_a = list(rank_hand(hand_a))
    ranks_hand_b = list(rank_hand(hand_b))
    # high card
    # maxranks = (max(t[1] for t in ranks_hand_a), max(t[1] for t in ranks_hand_b))
    winner_rank = None
    if ranks_hand_a and ranks_hand_b:
        rank_index_max_a = max(
            (rank_index, value) for rank_index, value in ranks_hand_a
        )
        rank_index_max_b = max(
            (rank_index, value) for rank_index, value in ranks_hand_b
        )
        if rank_index_max_a[0] > rank_index_max_b[0]:
            winner_rank = 0
        elif rank_index_max_a[0] < rank_index_max_b[0]:
            winner_rank = 1
        elif rank_index_max_a[0] == rank_index_max_b[0]:
            if rank_index_max_a[1] > rank_index_max_b[1]:
                winner_rank = 0
            elif rank_index_max_a[1] < rank_index_max_b[1]:
                winner_rank = 1
            elif rank_index_max_a[1] == rank_index_max_b[1]:
                pass

    elif ranks_hand_a:
        winner_rank = 0
    elif ranks_hand_b:
        winner_rank = 1
    highest_cards_pairs = [
        (a, b)
        for a, b in reversed(
            list(
                zip(
                    sorted([card_value_str(s) for s in hand_a]),
                    sorted([card_value_str(s) for s in hand_b]),
                )
            )
        )
        if a != b
    ]

    high_card_winner_pair = highest_cards_pairs[0]
    if high_card_winner_pair[0] == high_card_winner_pair[1]:
        raise Exception
    winner_high_card = None
    if high_card_winner_pair[0] > high_card_winner_pair[1]:
        winner_high_card = 0
    if high_card_winner_pair[0] < high_card_winner_pair[1]:
        winner_high_card = 1
    print(
        index if index is not None else "",
        hand_a,
        hand_b,
        winner_rank if winner_rank is not None else "x",
        winner_high_card,
        [(funcs_rank[t[0]].__name__, VALUES[t[1] - 1]) for t in ranks_hand_a],
        [(funcs_rank[t[0]].__name__, VALUES[t[1] - 1]) for t in ranks_hand_b],
        VALUES[high_card(hand_a) - 1],
        VALUES[high_card(hand_b) - 1],
    )
    if winner_rank:
        return winner_rank
    # if len(set(highest_cards)) == 1:
    #     print(highest_cards_pairs)
    #     raise Exception(set(VALUES[(c - 1)] for c in highest_cards))
    return winner_high_card
    # 217 wrong
    # 201 wrong
    # 219 wrong


def solve(filepath: Path, debug=False):
    c = Counter()
    count_winners = Counter()
    with open(filepath) as f:
        for index, l in enumerate(f):
            hands = line(l)
            # for f in reversed(funcs_rank):
            #     a = f(hands[0])
            #     b = f(hands[1])
            #     if a:
            #         c.update([f.__name__])
            #     if b:
            #         c.update([f.__name__])
            if index == 998:
                pass
            count_winners.update([winner(hands[0], hands[1], index=index)])
            # for h in hands:
            #     if all(s in "".join(h) for s in ["T", "J", "Q", "K", "A"]):
            #         print(l)
    print(count_winners)
    return count_winners[0]


def main():

    with TimingContext() as tc:
        s = solve(HANDS_FILE)
        print(s, tc.get_duration())
    with TimingContext() as tc:
        s = solve(HANDS_FILE_TEST)
        print(s, tc.get_duration())
    with TimingContext() as tc:
        s = solve(HANDS_FILE_TEST_2)
        print(s, tc.get_duration())


if __name__ == "__main__":
    main()

"""
ranks ['AD', '7D', 'JH', '6C', '7H'] ['4H', '3S', '3H', '4D', 'QH'] 0 0 [('one_pair', '7')] [('one_pair', '4'), ('two_pair', '4')] A Q
139 ['9D', 'TD', '9H', 'QC', '5D'] ['6C', '8H', '8C', 'KC', 'TS'] x 1 [('one_pair', '9')] [('one_pair', '8')] Q K
"""
