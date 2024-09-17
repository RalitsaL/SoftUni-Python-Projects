hour = int(input())
minutes = int(input())

hour_in_minutes = hour * 60
hour_in_15_minutes = hour_in_minutes + minutes + 15

final_hour = hour_in_15_minutes // 60
final_minutes = hour_in_15_minutes % 60

if final_hour >= 24:
    final_hour = final_hour - 24
if final_minutes <10:
    print(f"{final_hour}:0{final_minutes}")

else :
    print(f"{final_hour}:{final_minutes}")