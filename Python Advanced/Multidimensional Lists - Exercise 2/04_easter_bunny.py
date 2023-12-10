size = int(input())
field = [[int(x) if x.isnumeric() else x for x in input().split()] for _ in range(size)]

max_eggs = 0
best_path = []
best_direction = None
bunny = []

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'right': (0, 1),
    'left': (0, -1)
}

for row in range(size):
    if "B" in field[row]:
        bunny = [row, field[row].index("B")]

for direction, positions in directions.items():
    row, col = [
        bunny[0] + positions[0],
        bunny[1] + positions[1],
    ]
    path = []
    collected_eggs = 0

    while 0 <= row < size and 0 <= col < size:
        if field[row][col] == "X":
            break

        collected_eggs += int(field[row][col])
        path.append([row, col])

        row += positions[0]
        col += positions[1]

    if collected_eggs >= max_eggs:
        max_eggs = collected_eggs
        best_direction = direction
        best_path = path

print(best_direction)
print(*best_path, sep='\n')
print(max_eggs)
