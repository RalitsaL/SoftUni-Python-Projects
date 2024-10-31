rooms_number = int(input())
free_chairs = 0
free_chairs_check = True
for i in range(rooms_number):
    chairs_and_visitors = input().split()
    chairs = int(len(chairs_and_visitors[0]))
    visitors = int(chairs_and_visitors[1])
    if chairs >= visitors:
        free_chairs += chairs - visitors
    else:
        print(f"{abs(chairs - visitors)} more chairs needed in room {i + 1}")
        free_chairs_check = False

if free_chairs_check:
    print(f"Game On, {free_chairs} free chairs left")