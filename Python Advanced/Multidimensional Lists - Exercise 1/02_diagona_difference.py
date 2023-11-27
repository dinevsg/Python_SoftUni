n = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(n)]

primary = 0
secondary = 0

for r in range(n):
    primary += matrix[r][r]

for r in range(n):
    secondary += matrix[r][n - r - 1]

print(abs(primary - secondary))
