operator = input()
a = int(input())
b = int(input())


def multiply(a, b):
    return int(a * b)


def divide(a, b):
    if b != 0:
        return int(a / b)
    else:
        return "Error! Division by zero"


def add(a, b):
    return int(a + b)


def subtract(a, b):
    return int(a - b)


if operator == "multiply":
    print(multiply(a, b))
elif operator == "divide":
    print(divide(a, b))
elif operator == "add":
    print(add(a, b))
elif operator == "subtract":
    print(subtract(a, b))