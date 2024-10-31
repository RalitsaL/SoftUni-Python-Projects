numbers = [int(digit) for digit in input().split(", ")]

current_group = 10

while len(numbers) > 0:
    current_list = [num for num in numbers if num <= current_group]
    print(f"Group of {current_group}'s: {current_list}")
    numbers = [num for num in numbers if num not in current_list]
    current_group += 10


