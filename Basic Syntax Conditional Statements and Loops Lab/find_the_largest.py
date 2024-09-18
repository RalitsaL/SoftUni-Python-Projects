number = input()
n = str(number)

from_smallest = sorted(n)
sorted_from_largest = sorted(n, reverse=True)

for d, digit in enumerate(sorted_from_largest):
    print(digit, end="")