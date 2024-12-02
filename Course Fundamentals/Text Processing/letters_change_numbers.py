my_string = input().split()
num_letter = 0
final_result = 0
for element in my_string:
    result_per_element = 0
    first_letter = element[0]
    last_letter = element[-1]
    number = int(element[1:-1])

    if first_letter.isupper():
        num_letter = (ord(first_letter) - 64)
        result_per_element = number / num_letter
    else:
        num_letter = (ord(first_letter) - 96)
        result_per_element = number * num_letter

    if last_letter.isupper():
        num_letter = (ord(last_letter) - 64)
        result_per_element -= num_letter
    else:
        num_letter = (ord(last_letter) - 96)
        result_per_element += num_letter

    final_result += result_per_element

print(f"{final_result:.2f}")