first_string = input()
my_list = first_string.split(" ")
countA = 0
countB = 0
flag = False
for index in range(1, 12):
    current_counter_A = my_list.count("A-" + str(index))
    current_counter_B = my_list.count("B-" + str(index))
    if current_counter_A > 0:
        countA += 1
    if current_counter_B > 0:
        countB += 1
    if countA > 4 or countB > 4:
        flag = True
        break

print(f"Team A - {11 - countA}; Team B - {11 - countB}")
if flag:
    print("Game was terminated")
