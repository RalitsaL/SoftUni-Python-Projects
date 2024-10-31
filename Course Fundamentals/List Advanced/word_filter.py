initial_input = input().split()
new_list = [i for i in initial_input if len(i) % 2 == 0]
for element in new_list:
    print(element)