n = int(input())
m = int(input())
s = int(input())

for nums in range(m, n - 1, -1):
    if nums % 2 == 0 and nums % 3 == 0:
        if nums == s:
            break
        else:
            print(nums, end=" ")