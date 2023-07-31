import sys
n = int(input())

total_sum = 0
max_num = -sys.maxsize

for i in range(1, n + 1):
    current_number = int(input())
    if current_number > max_num:
        max_num = current_number
    total_sum = total_sum + current_number

other_sum = total_sum - max_num

if other_sum == max_num:
    print("Yes")
    print(f"Sum = {max_num}")
else:
    diff = abs(max_num - other_sum)
    print("No")
    print(f"Diff = {diff}")
