numbers = input().split()
list_first = []
list_second = []
length_half_numbers_list = int(len(numbers) / 2)

for index in range(length_half_numbers_list):
    list_first.append(numbers[index])
    list_second.append(numbers[-index - 1])

time_first = 0
time_second = 0



for element1 in list_first:
    if int(element1) == 0:
           time_first = time_first * 0.8
    time_first += int(element1)

for element in list_second:
    if int(element) == 0:
        time_second = time_second * 0.8
    time_second += int(element)

if time_first < time_second:
    print(f"The winner is left with total time: {time_first:.1f}")
else:
    print(f"The winner is right with total time: {time_second:.1f}")