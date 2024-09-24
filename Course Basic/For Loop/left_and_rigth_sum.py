numbers = int(input())

first_sum = 0
second_sum = 0

for new_num in range(numbers * 2):
    num = int(input())
    if new_num < numbers:
        first_sum += num
    else:
        second_sum += num

if first_sum == second_sum:
    print(f"Yes, sum = {first_sum}")
else:
    diff = abs(first_sum - second_sum)
    print(f"No, diff = {diff}")