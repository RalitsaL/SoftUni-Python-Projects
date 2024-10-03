cards = input().split()
count_shuffles = int(input())

for current_shuffle in range(count_shuffles):
    half_len_cards = len(cards) // 2
    left_cards = cards[:half_len_cards]
    right_cards = cards[half_len_cards:]
    new_list_after_shuffle = []

    for element in range(half_len_cards):

        new_list_after_shuffle.append(left_cards[element])
        new_list_after_shuffle.append(right_cards[element])
    cards = new_list_after_shuffle.copy()

print(cards)
