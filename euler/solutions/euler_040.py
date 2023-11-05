"""
0.12345678910111213
"""
from .utils import numprod

target_indices = (1, 10, 100, 1000, 10000, 100000, 1000000)


def smallest_ndigit(n):
    return 10 ** (n - 1)


def largest_ndigit(n):
    return 10 ** (n) - 1


def how_many_n_digit(n):
    return largest_ndigit(n) + 1 - smallest_ndigit(n)


def digit_length_of_all_ndigits(n):
    return how_many_n_digit(n) * n


def get_digit_index_upper_bound(n, b=0, d=1):
    if b >= n:
        return b
    b_new = digit_length_of_all_ndigits(d)
    return get_digit_index_upper_bound(n, b + b_new, d + 1)


def get_digit_length_from_index(index, d=1):
    dl = digit_length_of_all_ndigits(d)
    if dl >= index:
        return index, d
    return get_digit_length_from_index(index - dl, d + 1)


def decode_index_digitlength(index, d):
    """
    How many d-digit numbers to concatenate to reach a length of at least index?
    """
    index_0 = index
    a = (
        index_0 // d
    )  # a= how many d-digit numbers precede the d-digit number containing our target digit
    b = index_0 % d  # answer is bth digit of a+1th d-digit number
    start = 10 ** (d - 1)
    final_ddigit = smallest_ndigit(d) + a
    digit_target = str(final_ddigit)[b]
    return int(digit_target)


def champerowne_nth(n):
    n_final = n - 1
    t = get_digit_length_from_index(n_final)
    return decode_index_digitlength(*t)


def main():
    for i in range(1, 1000):
        print(i, get_digit_index_upper_bound(i), get_digit_length_from_index(i))
    print([get_digit_length_from_index(i) for i in target_indices])
    print([champerowne_nth(i) for i in range(100)])
    assert len(target_indices) == 7
    for i in range(1, 10):
        assert champerowne_nth(i) == i, f"{i}, {champerowne_nth(i)}"
    assert champerowne_nth(12) == 1
    assert champerowne_nth(13) == 1
    assert champerowne_nth(14) == 1
    assert champerowne_nth(15) == 2
    assert champerowne_nth(16) == 1
    assert champerowne_nth(17) == 3
    assert champerowne_nth(18) == 1
    solution_digits = [champerowne_nth(i) for i in target_indices]

    print(numprod(solution_digits), solution_digits)


if __name__ == "__main__":
    main()
