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


def get_diagonals(matrix):
    pass


def main():
    with open('resources/p081_matrix.txt') as f:
        s = f.read()
    matrix = list()
    matrix = [list(map(int, line.split(',')))
              for line in s.split('\n') if len(line.strip()) > 0]
    print(matrix)


if __name__ == '__main__':
    main()
