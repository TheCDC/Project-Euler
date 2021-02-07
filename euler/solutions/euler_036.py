from euler.solutions.utils import digits


def test(n):
    b10 = digits(n, 10)
    b2 = digits(n, 2)
    # print(b10,b2)
    return (b10 == b10[::-1]) and (b2 == b2[::-1])


s = 0
for i in range(1000000):
    if test(i):
        s += i
        # print(i)
print(s)
