num = int(input())
sum_chars = 0

for chars in range(num):
    chars = input()
    sum_chars += ord(chars)

print(f"The sum equals: {sum_chars}")
