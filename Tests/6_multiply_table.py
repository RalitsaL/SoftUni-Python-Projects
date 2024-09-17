number = input()

first_digit = int(number[2])
second_digit = int(number[1])
third_digit = int(number[0])

for i in range(1, first_digit + 1):
    for j in range(1, second_digit + 1):
        for k in range(1, third_digit + 1):
            result = i * j * k
            print(f"{i} * {j} * {k} = {result};")