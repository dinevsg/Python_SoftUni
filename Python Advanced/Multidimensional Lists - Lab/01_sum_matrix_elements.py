rows, cols = [int(x) for x in input().split(", ")]

matrix = [[int(i) for i in input().split(", ")] for x in range(rows)]

sum_matrix = 0

for row in range(rows):
    sum_matrix += sum(matrix[row])

print(sum_matrix)
print(matrix)
