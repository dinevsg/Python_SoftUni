n = int(input())
matrix = [[int(x) for x in input().split(", ")] for _ in range(n)]
flatten = []

for row in range(len(matrix)):
    for col in range(len(matrix[row])):
        flatten.append(matrix[row][col])
print(flatten)
