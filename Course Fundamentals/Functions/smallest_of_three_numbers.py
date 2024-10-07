a = int(input())
b = int(input())
c = int(input())


def smallest(list_with_numbers: list) -> int:
    return min(list_with_numbers)


smallest_num = smallest([a, b, c])
print(smallest_num)