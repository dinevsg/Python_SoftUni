pages = int(input())
pages_for_one_hour = int(input())
days_need_to_read = int(input())

hours_per_day = ((pages / pages_for_one_hour) / days_need_to_read)

print(int(hours_per_day))
