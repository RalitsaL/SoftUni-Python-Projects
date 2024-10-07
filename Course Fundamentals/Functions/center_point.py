import math


def distance_to_center(x, y):
    # Изчисляваме разстоянието на точка (x, y) до центъра (0, 0)
    return math.sqrt(x ** 2 + y ** 2)


def closest_point(x1, y1, x2, y2):
    # Изчисляваме разстоянията на двете точки до центъра
    dist1 = distance_to_center(x1, y1)
    dist2 = distance_to_center(x2, y2)

    # Сравняваме разстоянията и връщаме най-близката точка
    if dist1 <= dist2:
        # Първата точка е по-близо или на същото разстояние
        print(f"({math.floor(x1)}, {math.floor(y1)})")
    else:
        # Втората точка е по-близо
        print(f"({math.floor(x2)}, {math.floor(y2)})")


# Четем входните стойности
x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

# Извикваме функцията за намиране на най-близката точка
closest_point(x1, y1, x2, y2)