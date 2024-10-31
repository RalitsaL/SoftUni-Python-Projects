string1 = input().split(", ")
string2 = input().split(", ")
# output_list = []
# for element in string1:
#     for element2 in string2:
#         if element in element2:
#             output_list.append(element)

#print(list(dict.fromkeys(output_list)))

print([element for element in string1 if any(element in element2 for element2 in string2)])
