initial_input = input().split()
palindrome = input()
my_list = [i for i in initial_input if i == i[::-1]]
count_palindrome = 0

for i in range(len(my_list)):
    if my_list[i] == palindrome:
        count_palindrome += 1

print(my_list)
print(f"Found palindrome {count_palindrome} times")