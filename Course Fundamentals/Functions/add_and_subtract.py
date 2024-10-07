def sum_numbers(a:int, b:int) -> int:
    return a + b


def subtract(result:int, c:int) -> int:
    return result - c


def add_and_subtract(a, b, c) -> int:
    sum_result = sum_numbers(a, b)
    final_result = subtract(sum_result, c)
    return final_result


a = int(input())
b = int(input())
c = int(input())

print(add_and_subtract(a, b, c))

