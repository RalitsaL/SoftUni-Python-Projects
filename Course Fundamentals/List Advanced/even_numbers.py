my_list = list(map(int, input().split(", ")))
indexes_list = [index for index, value in enumerate(my_list) if value % 2 == 0]
print(indexes_list)