n = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(n)]

primary = [matrix[r][r] for r in range(n)]

print(sum(primary))
