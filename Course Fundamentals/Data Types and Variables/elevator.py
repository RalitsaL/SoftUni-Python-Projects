from math import ceil
n_peoples = int(input())
capacity = int(input())

courses = ceil(n_peoples / capacity)
print(courses)