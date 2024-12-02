file_name = input().split('\\')

needed_part = list(file_name[len(file_name) - 1:])
name = ""
extension = ""
for element in needed_part:
    for char in element:
        if char != ".":
            name += char

        if char == ".":
            break
    element = element[::-1]
    for char in element:
        if char != ".":
            extension += char
        if char == ".":
            break

extension = extension[::-1]

print(f"File name: {name}")
print(f"File extension: {extension}")


# import re
# file_path = input().split("\\")
# filename_and_extension = file_path[-1]
# filename, extension = filename_and_extension.split(".")
# print(f"File name: {filename}")
# print(f"File extension: {extension}")