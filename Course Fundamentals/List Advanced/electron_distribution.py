num_electrons = int(input())
final_list = []
sum_final_list = 0

for i in range(1, num_electrons + 1):
    current_num = 2*(i**2)

    if sum_final_list + current_num <= num_electrons:
        final_list.append(current_num)
        sum_final_list += current_num
    else:
        if sum_final_list == num_electrons:
            break
        else:
            final_list.append(num_electrons - sum_final_list)
        break

print(final_list)