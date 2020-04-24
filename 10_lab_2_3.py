#!/usr/bin/env python
# coding: utf-8

import sys
import os


def merge(x):
    if len(x) == 1:
        return x
    else:
        mid = int(len(x) / 2)
        l = merge(x[:mid])
        r = merge(x[mid:])
    i = j = 0
    result = []
    while i < len(l) and j < len(r):
        if l[i] < r[j]:
            result.append(l[i])
            i += 1
        else:
            result.append(r[j])
            j += 1
    result += l[i:]
    result += r[j:]
    return result


def amountOFsymbols(y):
    result = 0
    for i in y:
        result += len(i)
    return result


def merge2(x):
    if len(x) == 1:
        return x
    else:
        mid = int(len(x) / 2)
        l = merge2(x[:mid])
        r = merge2(x[mid:])
    i = j = 0
    result = []
    while i < len(l) and j < len(r):
        if amountOFsymbols(l[i]) < amountOFsymbols(r[j]):
            result.append(l[i])
            i += 1
        else:
            result.append(r[j])
            j += 1
    result += l[i:]
    result += r[j:]
    return result


def sort():
    answer = input('Input \'self\' or \'file\'\n')
    if answer == 'self':
        llist = []
        count = int(input('Введите количество строк\n'))
        for i in range(count):
            llist.append(merge(input('Введите строку\n').split(' ')))
    elif answer == 'file':
        llist = []
        file = open(input('Введите имя файла с расширением: '), 'r+')
        linesINfile = file.readlines()  # строки в файле
        count = len(linesINfile)
        for i in range(count):
            llist.append(merge(linesINfile))
        llist = llist[1]
    else:
        print('Invalid input!')
    llist = merge2(llist)
    text = ''

    for i in range(len(llist)):
        for word in llist[i]:
            text += ''.join(word) + ' '
        text += '\n'
    file = open('textfile_1.txt', 'tw', encoding='utf-8')
    file.write(text)
    file.close()


if __name__ == "__main__":
    sort()

