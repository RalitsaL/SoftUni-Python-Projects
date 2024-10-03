num = int(input())
code_word = input()
all_list = []
filtered_list = []

for _ in range(num):
    strings = input()
    all_list.append(strings)
    if code_word in strings:
        filtered_list.append(strings)

print(all_list)
print(filtered_list)
