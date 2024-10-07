import math


def distance_to_center(x, y):
    # Изчисляваме разстоянието на точка (x, y) до центъра (0, 0)
    return math.sqrt(x ** 2 + y ** 2)


def line_length(x1, y1, x2, y2):
    # Изчисляваме дължината на линия между точките (x1, y1) и (x2, y2)
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def longer_line(x1, y1, x2, y2, x3, y3, x4, y4):
    # Изчисляваме дължините на двете линии
    length1 = line_length(x1, y1, x2, y2)
    length2 = line_length(x3, y3, x4, y4)

    # Определяме по-дългата линия
    if length1 >= length2:
        # Ако първата линия е по-дълга или равна
        # Сравняваме разстоянията до центъра на двете точки
        if distance_to_center(x1, y1) <= distance_to_center(x2, y2):
            print(f"({math.floor(x1)}, {math.floor(y1)})({math.floor(x2)}, {math.floor(y2)})")
        else:
            print(f"({math.floor(x2)}, {math.floor(y2)})({math.floor(x1)}, {math.floor(y1)})")
    else:
        # Ако втората линия е по-дълга
        if distance_to_center(x3, y3) <= distance_to_center(x4, y4):
            print(f"({math.floor(x3)}, {math.floor(y3)})({math.floor(x4)}, {math.floor(y4)})")
        else:
            print(f"({math.floor(x4)}, {math.floor(y4)})({math.floor(x3)}, {math.floor(y3)})")


# Входните стойности за координатите на точките
x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x3 = float(input())
y3 = float(input())
x4 = float(input())
y4 = float(input())

# Извикваме функцията за намиране на по-дългата линия
longer_line(x1, y1, x2, y2, x3, y3, x4, y4)