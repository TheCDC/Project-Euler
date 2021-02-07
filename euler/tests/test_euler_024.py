from euler.solutions.euler_024 import pack, unpack, choose_by_unpacked


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
    assert pack([2, 1], [2, 10]) == 11


def test_pack_base_factorial3():
    assert pack([2, 1, 0], [3, 2, 1]) == 5
    assert pack([0, 1, 2], [3, 2, 1]) == 0


def test_pack_basefactorial():
    assert (
        pack([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        == 3628800 - 1
    )
    assert pack([9, 8, 7, 6, 5, 4, 3, 2, 1, 0], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 0


def test_unpack_base10():
    assert unpack(321, [10, 10, 10]) == [1, 2, 3]
    assert unpack(555, [10, 10, 10]) == [5, 5, 5]


def test_unpack_base16():
    assert unpack(0xABCD, [16, 16, 16, 16]) == [0xD, 0xC, 0xB, 0xA]


def test_unpack_factorial10():
    assert unpack(0, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [0] * 10


def test_choose_factorial2():
    """
    permute ABC

    ABC
    ACB
    BAC
    BCA
    CAB
    CBA
    """
    assert choose_by_unpacked(unpack(0, [1, 2, 3]), "abc") == ["a", "b", "c"]

    assert choose_by_unpacked(unpack(1, [1, 2, 3]), "abc") == ["a", "c", "b"]
    assert choose_by_unpacked(unpack(2, [1, 2, 3]), list(range(0, 3))) == [1, 0, 2]


def test_choose_factorial10():
    assert choose_by_unpacked(
        unpack(0, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), list(range(0, 10))
    ) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert choose_by_unpacked(
        unpack(1, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), list(range(0, 10))
    ) == [0, 1, 2, 3, 4, 5, 6, 7, 9, 8]
    assert choose_by_unpacked(
        unpack(2, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), list(range(0, 10))
    ) == [0, 1, 2, 3, 4, 5, 6, 8, 7, 9]
