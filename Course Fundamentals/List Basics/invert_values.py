string_list = input()
new_list = string_list.split()
new_list_int = [eval(i) for i in new_list]
reverse_list = []
for element in new_list_int:
    if element >= 0:
        element = -abs(element)
    else:
        element = abs(element)
    reverse_list.append(element)

print(reverse_list)