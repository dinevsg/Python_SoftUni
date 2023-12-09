def valid_idx(idx):
    return {info[0], info[2]}.issubset(valid_rows) and {info[1], info[3]}.issubset(valid_cols)


def swap_command(command, idx):
    if valid_idx(idx) and command == "swap" and len(idx) == 4:
        row1, col1, row2, col2 = idx
        matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]

        print(*[' '.join(r) for r in matrix], sep="\n")
    else:
        print("Invalid input!")


rows, cols = [int(x) for x in input().split()]
matrix = [input().split() for _ in range(rows)]

valid_rows = range(rows)
valid_cols = range(cols)

while True:
    command_type, *info = [int(x) if x.isdigit() else x for x in input().split()]
    if command_type == "END":
        break

    swap_command(command_type, info)
