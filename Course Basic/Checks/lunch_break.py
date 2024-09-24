from math  import ceil
series_name = str(input())
series_time = int(input())
lunch_break_time = int(input())

lunch = 1/8 * lunch_break_time
rest_time = 1/4 * lunch_break_time

free_time = lunch_break_time - lunch - rest_time

if free_time >= series_time:
    print(f"You have enough time to watch {series_name} and left with {ceil(free_time - series_time)} minutes free time.")

else:
    print(f"You don't have enough time to watch {series_name}, you need {ceil(series_time - free_time)} more minutes.")