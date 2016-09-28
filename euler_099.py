#!/usr/bin/env python3

import math


def val(b, e):
    return e * math.log(b)


def main():
    with open("p099_base_exp.txt") as f:
        contents = f.read()
    # lines
    cs = [(index + 1, val(*[int(j) for j in item.split(",")]))
          for index, item in enumerate(contents.split('\n'))]
    # print(cs)
    print(max(cs, key=lambda x: x[1])[0])

if __name__ == '__main__':
    main()
