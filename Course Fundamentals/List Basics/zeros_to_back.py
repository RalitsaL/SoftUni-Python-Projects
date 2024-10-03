string_input = input().split(", ")
int_input = [int(i) for i in string_input]
for i in range(len(int_input) - 1, -1, -1):
    if int_input[i] == 0:
        int_input.pop(i)
        int_input.append(0)

print(int_input)