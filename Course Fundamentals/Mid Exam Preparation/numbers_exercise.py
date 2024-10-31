my_list = list(map(int, input().split()))
length_list = len(my_list)
average_num = sum(my_list) / length_list
print_final_list = True

new_list = sorted([i for i in my_list if i > average_num], reverse=True)
if len(new_list) != 0:
    if len(new_list) > 5:
        new_list = new_list[:5]

    print(" ".join(map(str, new_list)))
else:
    print("No")