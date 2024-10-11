import sys


def main(n: int, m: int):
    if n == 1:
        print('1')
        return
    
    path = '1'
    first = 1

    while True:
        first = first + m - 1
        if first != n:
            first %= n

        if first == 1:
            break

        path += str(first)

    print(path)
    


if __name__ == '__main__':
    assert len(sys.argv) >= 3, "Программа ожидает на вход два обязательных аргумента!"
    
    n, m = map(int, (sys.argv[1], sys.argv[2]))
    assert n > 0 and m > 0, "Числа n и m должны быть положительными числами больше нуля!"
    
    main(n, m)