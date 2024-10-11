import sys
from math import sqrt

def get_circle(filename: str):
    """Получает координаты центра окружности и её радиус"""
    with open(filename, 'r') as file:
        x, y = map(int, file.readline().split())
        radius = int(file.readline())
    
    return x, y, radius


def get_points(filename: str):
    """Получает массив точек"""
    with open(filename, 'r') as file:
        return [tuple(map(int, line.split())) for line in file.readlines()]


def main(file_circle: str, file_points: str):
    circle_x, circle_y, radius = get_circle(file_circle)
    points = get_points(file_points)

    for point in points:
        x, y = point

        # Делаем смещение точки относительно центра окр. если бы он находился в (0, 0)
        x = x - circle_x
        y = y - circle_y

        # Определяем расстояние от точки до центра окружности (по т. Пифагора)
        distance = sqrt(x ** 2 + y ** 2)

        # На основе расстояния определяем положение точки относительно окружности
        if distance == radius:  # лежит на окружности
            print('0')
        elif distance < radius:  # лежит внутри окружности
            print('1')
        else:  # лежит снаружи окружности
            print('2')
            

if __name__ == '__main__':
    assert len(sys.argv) >= 3, "Программа ожидает на вход два обязательных аргумента!"
    
    main(sys.argv[1], sys.argv[2])