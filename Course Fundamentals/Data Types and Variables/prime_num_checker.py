num = int(input())
flag = True
for all_nums in range(2, num):
    if num % all_nums == 0:
        print("False")
        flag = False
        break
if num <= 0:
    print(False)
elif flag:
    print(True)