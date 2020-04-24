# coding: utf-8
def leon(n):
    fib1 = 1
    fib2 = 1
    i = 0
    while i < n - 2:
        fib_sum = fib1 + fib2
        fib1 = fib2
        fib2 = fib_sum
        i = i + 1
    return fib2
    a = fib(n)
    leo = 2 * a - 1
    return leo


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
            print(leon(int(n)))


if __name__ == "__main__":
    main()
