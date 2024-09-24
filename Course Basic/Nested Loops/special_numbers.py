N = int(input())
is_found = False
for num in range(1111, 9999 + 1):
    num_to_str = str(num)
    for digit in num_to_str:
        if int(digit) == 0:
            is_found = False
            break
        elif N % int(digit) == 0:
            is_found = True
        else:
            is_found = False
            break

    if is_found:
        print(num, end=" ")

