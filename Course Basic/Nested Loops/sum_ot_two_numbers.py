interval_start = int(input())
interval_stop = int(input())
magic_num = int(input())
combination_counter = 0
flag = ""
for a in range(interval_start, interval_stop + 1):
    for b in range(interval_start, interval_stop + 1):
        combination_counter +=1
        if a + b == magic_num:
            print(f"Combination N:{combination_counter} ({a} + {b} = {magic_num})")
            flag = True
            break

    if flag:
        break

else:
    print(f"{combination_counter} combinations - neither equals {magic_num}")
