from euler.solutions.euler_024 import nth_permutation, pack, unpack, choose_by_unpacked
from euler.solutions.utils import factorial


def test_pack_base10():
    assert pack([1], [10]) == 1
    assert pack([9], [10]) == 9
    assert pack([1, 0], [10, 10]) == 10
    assert pack([1, 1, 0], [10, 10, 10]) == 110


def test_pack_base2():
    assert pack([1, 1, 1], [2, 2, 2]) == 0b111
    assert pack([1, 0, 1], [2, 2, 2]) == 0b101
    assert (
        pack([1, 0, 1, 0, 0, 1, 0, 1, 0, 0], [2, 2, 2, 2, 2, 2, 2, 2, 2, 2])
        == 0b1010010100
    )


def test_pack_base16():
    assert pack([1, 1, 1], [16] * 3) == 0x111
    assert pack([1, 0, 1], [16] * 3) == 0x101
    assert pack([0xA, 0xB, 0xC, 0xD], [16] * 4) == 0xABCD


def test_pack_mixed_radix():
    assert pack([1, 3, 0, 0, 0], [5, 4, 3, 2, 1]) == 42


def test_pack_example():
    # Decimal system
    assert pack([4, 2], [10, 10]) == 42

    # Binary system
    assert pack([1, 0, 1, 0, 1, 0], [2, 2, 2, 2, 2, 2]) == 42

    # Factorial system
    assert pack([1, 3, 0, 0, 0], [5, 4, 3, 2, 1]) == 42


def test_pack_base_factorial3_last():
    assert pack([0, 1, 2], [1, 2, 3]) == 5


def test_unpack_base10():
    assert unpack(321, [10, 10, 10]) == [3, 2, 1]
    assert unpack(555, [10, 10, 10]) == [5, 5, 5]


def test_unpack_base16():
    assert unpack(0xABCD, [16, 16, 16, 16]) == [
        0xA,
        0xB,
        0xC,
        0xD,
    ]


def test_unpack_factorial10():
    assert unpack(0, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [0] * 10


def test_pack_unpack():
    assert unpack(pack([4, 2], [10, 10]), [10, 10]) == [4, 2]


def test_solution():
    assert nth_permutation(
        list(range(10)), 999999, [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    ) == [2, 7, 8, 3, 9, 1, 5, 4, 6, 0]
