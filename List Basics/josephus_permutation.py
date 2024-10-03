circle = input().split(' ')
k = int(input())
result = []
counter = 0

i = 0
while len(circle) > 0:
    counter += 1

    if counter % k == 0:
        result.append(circle.pop(i))
    else:
        i += 1

    if i >= len(circle):
        i = 0

print(str(result).replace(' ', '').replace('\'', ''))