num = int(input())
flag = True
for _ in range(1, num +1):
    number = int(input())
    if number % 2 == 0:
        continue
    else:
        print(f"{number} is odd!")
        flag = False
        break
if flag:
    print("All numbers are even.")