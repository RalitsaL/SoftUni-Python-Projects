numbers = list(map(int, input().split()))


def even_nums(num):
    if num % 2 == 0:
        return True
    else:
        return False


even_numbers_only = filter(even_nums, numbers)
only_even_list = []

for i in even_numbers_only:
    only_even_list.append(i)


print(only_even_list)
