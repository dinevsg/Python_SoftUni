days_off = int(input())

rest_needed = 30000
play_at_work = (365 - days_off) * 63
play_at_day_off = days_off * 127
total = play_at_day_off + play_at_work

if rest_needed < total:
    print(f"Tom will run away")
    print(f"{abs(rest_needed - total) // 60} hours and {abs(rest_needed - total) % 60} minutes more for play")

elif rest_needed >= total:
    print(f"Tom sleeps well")
    print(f"{(rest_needed - total) // 60} hours and {(rest_needed - total) % 60} minutes less for play")
