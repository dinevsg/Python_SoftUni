init_hour = int(input())
init_min = int(input())

total_minutes = (init_hour * 60) + init_min + 15
hour = total_minutes // 60
minutes = total_minutes % 60

if hour > 23:
    hour = 0

if minutes < 10:
    print(f'{hour}:0{minutes}')
else:
    print(f'{hour}:{minutes}')
