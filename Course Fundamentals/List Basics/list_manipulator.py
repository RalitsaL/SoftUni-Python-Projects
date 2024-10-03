my_list = list(map(int,input().split()))
my_list_copy = my_list.copy()
is_there_even_element = any(el % 2 == 0 for el in my_list)
is_there_odd_element = any(el % 2 == 1 for el in my_list)

while True:
    command = input().split()
    first_list = []
    last_list = []

    if "end" in command:
        break

    elif "exchange" in command:
        index = int(command[1])
        if 0 <= index < len(my_list):
            first_half = my_list[:index + 1]
            second_half = my_list[index + 1:]
            my_list = second_half + first_half
        else:
            print("Invalid index")

    elif "max" in command:
        if "even" in command:
            if is_there_even_element:
                max_even = max(i for i in my_list if i % 2 == 0)
                print(len(my_list) - 1 - my_list[::-1].index(max_even))
            else:
                print("No matches")
        elif "odd" in command:
            if is_there_odd_element:
                max_odd = max(i for i in my_list if i % 2 == 1)
                print(len(my_list) - 1 - my_list[::-1].index(max_odd))
            else:
                print("No matches")

    elif "min" in command:
        if "even" in command:
            if is_there_even_element:
                min_even = min(j for j in my_list if j % 2 == 0)
                print(len(my_list) - 1 - my_list[::-1].index(min_even))
            else:
                print("No matches")
        elif "odd" in command:
            if is_there_odd_element:
                min_odd = min(j for j in my_list if j % 2 == 1)
                print(len(my_list) - 1 - my_list[::-1].index(min_odd))
            else:
                print("No matches")

    elif "first" in command:
        index = int(command[1])
        if index > len(my_list):
            print("Invalid count")

        else:
            if "even" in command:
                if is_there_even_element:
                    for nums in my_list:
                        if nums % 2 == 0:
                            first_list.append(nums)
                    print(first_list[:index])
                else:
                    print(first_list)
            elif "odd" in command:
                if is_there_odd_element:
                    for nums in my_list:
                        if nums % 2 != 0:
                            first_list.append(nums)
                    print(first_list[:index])
                else:
                    print(first_list)
    elif "last" in command:
        index = int(command[1])
        if index > len(my_list):
            print("Invalid count")
        else:
            if "even" in command:
                if is_there_even_element:
                    for nums in my_list:
                        if nums % 2 == 0:
                            last_list.append(nums)
                    print(last_list[-index:])
                else:
                    print(last_list)
            elif "odd" in command:
                if is_there_odd_element:
                    for nums in my_list:
                        if nums % 2 != 0:
                            last_list.append(nums)
                    print(last_list[-index:])
                else:
                    print(last_list)

print(my_list)

