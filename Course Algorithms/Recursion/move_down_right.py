def unique_paths_recursive(m, n):
    if m == 1 or n == 1:
        return 1
    if m == 0 or n == 0:
        return 0

    return unique_paths_recursive(m - 1, n) + unique_paths_recursive(m, n - 1)

m = int(input())
n = int(input())

print(unique_paths_recursive(m, n))