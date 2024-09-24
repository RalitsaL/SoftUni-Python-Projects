from math import pi
figure = str(input())
area = 0

if figure == "square":
    number = float(input())
    area = number * number

elif figure == "rectangle":
    number = float(input())
    number_two = float(input())
    area = number * number_two

elif figure == "circle":
    radius = float(input())
    area = radius * radius * pi

elif figure == "triangle":
    height = float(input())
    width = float(input())
    area = height * width / 2

print(f"{area:.3f}")