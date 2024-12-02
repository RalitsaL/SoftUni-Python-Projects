def linear_search(arr, target):
    for idx, num in enumerate(arr):
        if num == target:
            return idx
    return "Not found"

nums = [1, 2, 3,4 ,5,58 ,6,76, 7]
target = 3

print(linear_search(nums, target))