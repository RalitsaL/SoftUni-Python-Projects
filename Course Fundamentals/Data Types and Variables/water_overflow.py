num_lines = int(input())
capacity = 255
is_full = False

for lines in range(num_lines):

    litres = int(input())

    if capacity - litres < 0:
        print("Insufficient capacity!")
        continue
    capacity -= litres


print(255 - capacity)


