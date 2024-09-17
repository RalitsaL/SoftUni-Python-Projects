start_from = input()
end_at = input()

for digit1 in range(int(start_from[0]), int(end_at[0])+1):
    for digit2 in range(int(start_from[1]), int(end_at[1])+1):
        for digit3 in range(int(start_from[2]), int(end_at[2])+1):
            for digit4 in range(int(start_from[3]), int(end_at[3])+1):
                if digit1 % 2 != 0 and digit2 % 2 != 0 and digit3 % 2 != 0 and digit4 % 2 != 0:
                    print(f"{digit1}{digit2}{digit3}{digit4}", end = " ")
