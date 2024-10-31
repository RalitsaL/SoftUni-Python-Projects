distances = list(map(int, input().split()))

result = 0
catched_pokemons = 0
while True:

    number_pokemons = len(distances)
    if number_pokemons == 0:
        break

    index_received = int(input())

    if index_received < 0:
        current_num = distances[0]
        distances.pop(0)
        distances.insert(0, distances[-1])
    elif index_received >= len(distances):
        current_num = distances[-1]
        distances.pop(-1)
        distances.insert(len(distances), distances[0])
    else:
        current_num = distances[index_received]
        distances.pop(index_received)

    for i in range(len(distances)):
        if distances[i] <= current_num:
            distances[i] += current_num
        else:
            distances[i] -= current_num

    result += current_num


print(result)
