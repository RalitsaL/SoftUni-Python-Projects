start = int(input())
end = int(input())

for index in range(start, end + 1):
    chars = chr(index)
    if index == end:
        print(chars)
    else:
        print(chars, end=" ")