rows, cols = [int(x) for x in input().split(", ")]
matrix = [[int(x) for x in input().split()] for _ in range(rows)]

for col in range(cols):
    sum_col = 0

    for row in range(rows):
        sum_col += matrix[row][col]
    print(sum_col)

