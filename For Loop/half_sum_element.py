from sys import maxsize
n = int(input())
max_number = -maxsize
sum_number = 0
for num in range(n):
    new_number = int(input())
    if new_number > max_number:
        max_number = new_number
    sum_number += new_number

if max_number == sum_number - max_number:
    print(f"Yes\nSum = {max_number}")
else:
    print(f"No\nDiff = {abs(max_number - (sum_number - max_number))}")


