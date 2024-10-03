factor = int(input())
count = int(input())

my_list = []

for elements in range(1, count + 1):
    new_element = factor * elements
    my_list.append(new_element)

print(my_list)