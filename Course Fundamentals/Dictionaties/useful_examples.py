nums = {1: "one", 2: "two", 3: "three", 33: "three", 4: "four", 5: "five"}


for key in nums.keys(): # going through all keys
    print(key)

for value in nums.values(): # going through all values
    print(value)

for key, value in nums.items(): #going through both keys and values
    print(key, value)

nums[4] = "four" # adding new element
print(nums)

searched_value = "three"
for key, value in nums.items(): #return all keys that are connected to the value
    if value == searched_value:
        print(key)

if searched_value in nums.values(): #just checking if we have such value
    print("it is presented in the dictionary")

value = nums.pop(1)  # remove and safe the element from dict (if print - will print the value)
print(value)
value1 = nums.popitem() # removes and save the last added element
print(value1)
key, value2 = nums.popitem() #will show both key and value
print(key, value2)


input = "3 5 5 hi pi HO Hi 5 ho 3 hi pi"
word_keys = [x.lower() for x in input.split()]  # input().lower().split()
count = 0
occurrences = dict.fromkeys(word_keys, count)
for word in word_keys:
    occurrences[word] += 1
    # occurrences[word] = word_keys.count(word) #same
print(occurrences)


for word, countt in occurrences.items():
    if countt % 2 != 0:
        print(word, end=" ")



ex_list = [100, 200, 300]
ex_dict = {index: element for index, element in enumerate(ex_list)}
print(ex_dict)

example_char = "s, o, m, e, i, n, p, u, t".split(", ")
char_dict = {char: ord(char) for char in example_char}
print(char_dict)


a = {1: "one"}
b = {2: "two"}
a.update(b)
print(a)

nums = [1, 2, 3]
nums2 = [11, 22, 33]
info = dict(zip(nums, nums2))
print(info)
for num, num2 in info.items():
    print(f"{num} -> {num2}")