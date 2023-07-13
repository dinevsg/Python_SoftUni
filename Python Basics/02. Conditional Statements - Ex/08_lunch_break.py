from math import ceil

serial_name = input()
episode_length = int(input())
break_length = int(input())

lunch_time = break_length / 8
rest_time = break_length / 4

time_left = break_length - lunch_time - rest_time
diff = abs(time_left - episode_length)
rounded_diff = ceil(diff)

if time_left >= episode_length:
    print(f'You have enough time to watch {serial_name} and left with {rounded_diff:} minutes free time.')
else:
    print(f"You don't have enough time to watch {serial_name}, you need {rounded_diff} more minutes.")
