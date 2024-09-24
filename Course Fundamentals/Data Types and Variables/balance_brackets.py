lines = int(input())
two_consecutive = ""
start_with_closing = False
last_bracket = ""
counter_left = 0
counter_right = 0
for index in range(lines):

    line = input()

    if line == "(":
        counter_left += 1
        if counter_left > 1:
            two_consecutive = True
            break
    elif line == ")":
        counter_right += 1
        if counter_right > 1:
            two_consecutive = True
            break
        elif last_bracket == "":
            start_with_closing = True

    else:
        continue
    last_bracket = line

    if counter_left == 1 and counter_right == 1:
        counter_left = 0
        counter_right = 0
if two_consecutive or start_with_closing:
    print("UNBALANCED")
elif counter_left == counter_right:
    print("BALANCED")
else:
    print("UNBALANCED")
