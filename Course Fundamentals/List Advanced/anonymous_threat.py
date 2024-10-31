initial_string = input().split()

while True:
    command = input()
    if command == "3:1":
        break
    command = command.split()
    action = command[0]
    start_index = index = int(command[1])
    end_index = partitions = int(command[2])
    len_list = len(initial_string)

    if start_index < 0:
        start_index = 0
    elif end_index > len_list:
        end_index = len_list

    if action == "merge":
        initial_string[start_index: end_index + 1] = ["".join(initial_string[start_index: end_index +1])]

    if action == "divide":
        word_to_split = initial_string[index]
        initial_string.pop(index)

        parts_length = len(word_to_split) // partitions
        extra_chars = len(word_to_split) % partitions

        new_parts = []
        start = 0
        what_is_left_from_word = len(word_to_split)

        for i in range(partitions):
            end = start + parts_length
            what_is_left_from_word -= parts_length
            if what_is_left_from_word <= parts_length:
                end = start + parts_length + extra_chars
                new_parts.append(word_to_split[start:end])
            else:
                new_parts.append(word_to_split[start:end])
            start = end

        initial_string[index:index] = new_parts


print(" ".join(initial_string))