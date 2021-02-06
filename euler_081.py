"""

Path sum: two ways
Problem 81

In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right, by only moving to the right and down, is indicated in bold red and is equal to 2427.

(131)     673     234     103     18
(201)     (96)    (342)   965     150
630       803     (746)   (422)   111
537       699     497     (121)   956
805       732     524     (37)    (331)


Find the minimal path sum, in matrix.txt (right click and "Save Link/Target As..."), a 31K text file containing a 80 by 80 matrix, from the top left to the bottom right by only moving right and down.
"""

EXAMPLE = [
    [131, 673, 234, 103, 18, ],
    [201, 96, 342, 965, 150, ],
    [630, 803, 746, 422, 111, ],
    [537, 699, 497, 121, 956, ],
    [805, 732, 524, 37, 331, ],

]


def transpose(l):
    return list(map(list, zip(*l)))


def get_diagonals(matrix):
    t = transpose(matrix)
    for col in range(len(matrix)):
        head = [None]*col
        tail = [None]*(len(t)-col-1)
        t[col] = head + t[col] + tail
    t = transpose(t)
    offsets = [0, -1]
    while len(t) > 1:
        # print(t)
        lastrow = t.pop()
        for i in range(len(lastrow)):
            pair = [val for val in lastrow[i:i+2] if val is not None]
            # print(pair,end=' ')
            # print(' '*i, pair, t[-1][i])
            if len(pair) == 0 or t[-1][i] is None :
                continue
            t[-1][i] += min(pair)

    return t[0][0]


def main():
    with open('resources/p081_matrix.txt') as f:
        s = f.read()
    matrix = list()
    matrix = [list(map(int, line.split(',')))
              for line in s.split('\n') if len(line.strip()) > 0]
    small_matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    # matrix = EXAMPLE
    print(get_diagonals(matrix))


if __name__ == '__main__':
    main()
