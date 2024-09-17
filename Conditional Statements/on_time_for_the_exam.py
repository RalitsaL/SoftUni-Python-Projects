exam_hour = int(input())
exam_minutes = int(input())
arrival_hour = int(input())
arrival_minutes = int(input())

exam_time_in_minutes = (exam_hour * 60) + exam_minutes
arrival_time_in_minutes = (arrival_hour * 60) + arrival_minutes
difference_in_hours_if_early = (exam_time_in_minutes - arrival_time_in_minutes) // 60
difference_in_minutes_if_early = (exam_time_in_minutes - arrival_time_in_minutes) % 60
difference_in_hours_if_late = (arrival_time_in_minutes - exam_time_in_minutes) // 60
difference_in_minutes_if_late = (arrival_time_in_minutes - exam_time_in_minutes) % 60

if exam_time_in_minutes == arrival_time_in_minutes:
    print("On time")

elif 0 < exam_time_in_minutes - arrival_time_in_minutes <= 30:
    print("On time")
    print(f"{exam_time_in_minutes - arrival_time_in_minutes} minutes before the start")

elif exam_time_in_minutes - arrival_time_in_minutes > 30:
    print("Early")
    if exam_time_in_minutes - arrival_time_in_minutes < 60:
        print(f"{exam_time_in_minutes - arrival_time_in_minutes} minutes before the start")
    else:
        print(f"{difference_in_hours_if_early}:{difference_in_minutes_if_early:02d} hours before the start")

elif exam_time_in_minutes < arrival_time_in_minutes:
    print("Late")
    if arrival_time_in_minutes - exam_time_in_minutes < 60:
        print(f"{arrival_time_in_minutes - exam_time_in_minutes} minutes after the start")
    else:
        print(f"{difference_in_hours_if_late}:{difference_in_minutes_if_late:02d} hours after the start")
