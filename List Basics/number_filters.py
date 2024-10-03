even = "even"
odd = "odd"
positive = "positive"
negative = "negative"
num = int(input())

all_numbers = [int(input()) for _ in range(num)]

command = input()
filtered_numbers = []
for nums in all_numbers:
    filter_command = (
        (command == even and nums % 2 == 0) or
        (command == odd and nums % 2 != 0) or
        (command == positive and nums >= 0) or
        (command == negative and nums < 0)
    )
    if filter_command:
        filtered_numbers.append(nums)

print(filtered_numbers)