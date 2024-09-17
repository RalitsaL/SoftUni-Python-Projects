start = input()
end = input()
to_exclude = input()
combinations = 0
chars = range(ord(start), ord(end) +1)
for letter1 in chars:
    if letter1 == ord(to_exclude):
        continue
    for letter2 in chars:
        if letter2 == ord(to_exclude):
            continue
        for letter3 in chars:
            if letter3 == ord(to_exclude):
                continue
            combinations += 1
            print(f"{chr(letter1)}{chr(letter2)}{chr(letter3)}", end=" ")
print(combinations)