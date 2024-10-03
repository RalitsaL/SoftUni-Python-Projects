tail = input()
body = input()
head = input()

full_view = [tail, body, head]
full_view[0], full_view[2] = full_view[2], full_view[0]
#full_view = [head, body, tail]
print(full_view)