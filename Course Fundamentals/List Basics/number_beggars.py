numbers_string = input().split(", ")
beggars = int(input())

list_numbers_int = [eval(i) for i in numbers_string]
start_index = 0
list_beggars_sum = []

for current_beggar in range(beggars):
    current_beggar_sum = sum(list_numbers_int[start_index::beggars])
    list_beggars_sum.append(current_beggar_sum)
    start_index += 1
print(list_beggars_sum)