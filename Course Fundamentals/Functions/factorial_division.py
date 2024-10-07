n1 = int(input())
n2 = int(input())


def factorial_division(num_1: int, num_2: int):
    factorial_division_1 = 1
    factorial_division_2 = 1
    for i in range(num_1, 0, -1):
        factorial_division_1 *= i
    for j in range(num_2, 0, -1):
        factorial_division_2 *= j

    division = factorial_division_1 / factorial_division_2
    return f"{division:.2f}"


print(factorial_division(n1, n2))