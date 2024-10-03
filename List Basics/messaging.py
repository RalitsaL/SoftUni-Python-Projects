string_numbers = input().split()
input_string = input()
length = len(input_string)
message = ""
count = 0
for i in string_numbers:
    count = sum(int(digit) for digit in str(i))
    index = count % length
    message += input_string[index]
    input_string = input_string[:index] + input_string[index + 1:]

print(message)

