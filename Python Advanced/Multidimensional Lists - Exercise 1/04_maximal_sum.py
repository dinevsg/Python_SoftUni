rows, cols = [int(x) for x in input().split()]

matrix = [[int(x) for x in input().split()] for row in range(rows)]

max_sum = float("-inf")
biggest_matrix = []

for row in range(rows - 2):
    for col in range(cols - 2):
        first = matrix[row][col:col + 3]
        second = matrix[row + 1][col:col + 3]
        third = matrix[row + 2][col:col + 3]

        current_sum = sum(first) + sum(second) + sum(third)
        if current_sum > max_sum:
            max_sum = current_sum
            biggest_matrix = [first, second, third]

print(f"Sum = {max_sum}")
[print(*row) for row in biggest_matrix]
