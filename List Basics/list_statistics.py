num = int(input())
list_positives = []
list_negatives = []

for _ in range(num):
    new_num = int(input())
    if new_num >= 0:
        list_positives.append(new_num)

    else:
        list_negatives.append(new_num)

count_positives = len(list_positives)
sum_negatives = sum(list_negatives)
print(list_positives)
print(list_negatives)
print(f"Count of positives: {count_positives}")
print(f"Sum of negatives: {sum_negatives}")

