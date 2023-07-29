number_of_line = int(input()) * 2

left_sum = 0
right_sum = 0

for x in range(1, int(number_of_line / 2) + 1):
    left_sum += int(input())

for y in range(int(number_of_line / 2), number_of_line):
    right_sum += int(input())

if left_sum == right_sum:
    print(f"Yes, sum = {left_sum}")
else:
    diff = abs(left_sum - right_sum)
    print(f"No, diff = {diff}")
