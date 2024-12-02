def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid_index = (left + right) // 2
        mid_element = arr[mid_index]

        if mid_element == target:
            return mid_index
        if target > mid_element:
            left = mid_index + 1
        else:
            right = mid_index - 1
    return -1
nums = [int(i) for i in input().split()]
target = int(input())

print(binary_search(nums, target))