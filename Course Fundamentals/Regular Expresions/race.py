import re

names = input().split(", ")
dict_participants = {}
while True:
    command = input()
    if command == "end of race":
        break
    name_pattern = r"[A-Za-z]"
    name = re.findall(name_pattern, command)
    km_pattern = r"[0-9]"
    km = re.findall(km_pattern, command)
    km_int = sum([int(i) for i in km])
    if "".join(name) in names:
        if "".join(name) in dict_participants:
            dict_participants["".join(name)] += km_int
        else:
            dict_participants["".join(name)] = km_int

myList = sorted(dict_participants, key=dict_participants.get, reverse=True) # sort by highest value
print(f"1st place: {myList[0]}")
print(f"2nd place: {myList[1]}")
print(f"3rd place: {myList[2]}")