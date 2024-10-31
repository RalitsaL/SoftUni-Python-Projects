total_peoples = int(input())
initial_lift_state = list(map(int, input().split()))
current_lift_state = initial_lift_state[:]

for i in range(len(current_lift_state)):
    value_current_seat = current_lift_state[i]
    if total_peoples == 0:
        break
    else:
        to_add = 4 - value_current_seat
        if to_add > 0:
            if total_peoples >= to_add:
                current_lift_state[i] = 4
                total_peoples -= to_add
            else:
                current_lift_state[i] += total_peoples
                total_peoples = 0

if total_peoples == 0 and sum(current_lift_state) == 4 * len(current_lift_state):
    pass
elif sum(current_lift_state) < 4 * len(current_lift_state):
    print("The lift has empty spots!")
elif total_peoples > 0:
    print(f"There isn't enough space! {total_peoples} people in a queue!")

print(" ".join(map(str, current_lift_state)))