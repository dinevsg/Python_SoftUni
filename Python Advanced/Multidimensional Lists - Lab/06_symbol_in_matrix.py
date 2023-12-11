n = int(input())
matrix = [[x for x in input()] for _ in range(n)]
symbol = input()
flag = False
for row in range(n):
    for col in range(n):
        if matrix[row][col] == symbol:
            flag = True
            print(f"({row}, {col})")
            break

    if flag:
        break

if not flag:
    print(f"{symbol} does not occur in the matrix")
