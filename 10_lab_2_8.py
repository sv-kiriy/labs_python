#!/usr/bin/env python
# coding: utf-8

# In[2]:


def check(n):
    s = 1
    x = 0
    while s <= n:
        s *= 2
        x += 1
        if s == n:
            print('Yes!')
            break
    else:
        print('No!')


def main():
    n = 1
    while n != 'exit':
        print("Введите число:  (P.S.напишите 'exit' для завершения программы): ")
        n = input()
        if n == 'exit':
            break
        elif not n.isnumeric():
            print("Некорректный ввод. Введите число:")
        else:
            check(int(n))


if __name__ == "__main__":
    main()
