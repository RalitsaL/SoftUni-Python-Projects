string_input = input()
nums = ""
letters = ""
other = ""

for symbol in string_input:
    if symbol.isalpha():
        letters += symbol
    elif symbol.isdigit():
        nums += symbol
    else:
        other += symbol

print(nums)
print(letters)
print(other)