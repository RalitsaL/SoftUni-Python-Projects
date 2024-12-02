initial_input = input().split()
str1 = initial_input[0]
str2 = initial_input[1]
chars_to_multiply = 0
total_sum = 0
longer = 0
if len(str1) > len(str2):
    chars_to_multiply = len(str2)

else:
    chars_to_multiply = len(str1)


for index in range(chars_to_multiply):
    total_sum += ord(str1[index])*ord(str2[index])

if len(str1) == len(str2):
    pass
elif len(str1) > len(str2):
    str1 = str1[chars_to_multiply:]
    for element in str1:
        total_sum += ord(element)
else:
    str2 = str2[chars_to_multiply:]
    for element in str2:
        total_sum += ord(element)
print(total_sum)