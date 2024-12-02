my_list = input().split(">")
new_list = []
ostatuk = 0
for element in my_list:

    if element[0].isdigit():
        if int(element[0]) == len(element):
            to_add = ""
            new_list.append(to_add)
        else:
            if int(element[0]) > len(element):
                to_add = ""
                new_list.append(to_add)
                ostatuk = int(element[0]) - len(element)
            else:
                element = element[ostatuk + int(element[0]):]
                new_list.append(element)

    else:
        to_add = element
        new_list.append(to_add)

print(">".join(new_list))