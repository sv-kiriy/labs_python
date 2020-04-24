#!/usr/bin/env python
# coding: utf-8

l = [1, 2, [2, 2, [2, [1, ['hello'], 3]], 22, [2, [2, 2]]]]


def flatten(x):
    for i in range(0, len(x)):
        yield (x[i])


def iterator(l):
    g = flatten(l)
    for i in range(0, len(l)):
        i = next(g)
        if i == Ellipsis:
            raise ValueError
        if type(i) != list:
            h.append(i)
        else:
            iterator(i)


if __name__ == "__main__":
    try:
        h = []
        iterator(l)
        print(h)
    except ValueError:
        print('Value Error')
