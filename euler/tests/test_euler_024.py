from euler.solutions import euler_024
def test_pack_base10():
    assert euler_024.pack(1,[10]) == 1
    assert euler_024.pack(9,[10]) == 9
    assert euler_024.pack(10,[10,10]) == 10
    assert euler_024.pack(10,[10,10]) == 10


def test_pack_base2():
    assert euler_024.pack(0b111,[2,2,2]) == 0b111
    assert euler_024.pack(0b101,[2,2,2]) == 0b101

def test_pack_base16():
    assert euler_024.pack(0x111,[2,2,2]) == 0x111
    assert euler_024.pack(0x101,[2,2,2]) == 0x101    