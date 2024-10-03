list_nums_str = input().split()
list_numbers_int = [eval(i) for i in list_nums_str]
nums_to_remove = int(input())
new_list = []
for number in range(nums_to_remove):
    smallest_num = min(list_numbers_int)
    list_numbers_int.remove(smallest_num)

print(", ".join(map(str, list_numbers_int)))

