my_text = input()

for index in range(len(my_text)):
    char = my_text[index]
    if char == ":" and index + 1 < len(my_text):
        emoticon = my_text[index + 1]
        print(f":{emoticon}")