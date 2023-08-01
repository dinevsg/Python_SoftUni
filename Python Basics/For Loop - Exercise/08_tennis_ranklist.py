import math

competitions = int(input())
start_points = int(input())

w_points = 2000
f_points = 1200
sf_points = 720
total_points = 0
win_count = 0

for i in range(1, competitions + 1):
    place = input()

    if place == "W":
        win_count += 1
        total_points = total_points + w_points
    elif place == "F":
        total_points = total_points + f_points
    elif place == "SF":
        total_points = total_points + sf_points

sum_points = total_points + start_points
average_points = total_points / competitions
rounded = math.floor(average_points)

per_win = win_count / competitions * 100

print(f"Final points: {sum_points}")
print(f"Average points: {rounded}")
print(f"{per_win:.2f}%")
