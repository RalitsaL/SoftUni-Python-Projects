numbers_all = input().split(", ")

positive_nums = [i for i in numbers_all if int(i) >= 0]
negative_nums = [i for i in numbers_all if int(i) < 0]
even_nums = [i for i in numbers_all if int(i) % 2 == 0]
odd_nums = [i for i in numbers_all if int(i) % 2 != 0]

print("Positive: " + ", ".join(positive_nums))
print("Negative: " + ", ".join(negative_nums))
print("Even: " + ", ".join(even_nums))
print("Odd: " + ", ".join(odd_nums))



