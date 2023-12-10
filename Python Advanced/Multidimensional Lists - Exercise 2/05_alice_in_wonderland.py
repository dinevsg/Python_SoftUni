size = int(input())

territory = []
alice_pos = []
collected_tea = 0

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(size):
    line = input().split()
    territory.append(line)

    if "A" in territory[row]:
        alice_pos = [row, territory[row].index("A")]
        territory[row][alice_pos[1]] = "*"

while collected_tea < 10:
    command = input()

    row = alice_pos[0] + directions[command][0]
    col = alice_pos[1] + directions[command][1]

    if not (0 <= row < size and 0 <= col < size):
        break

    alice_pos = [row, col]
    pos = territory[row][col]
    territory[row][col] = "*"

    if pos.isdigit():
        collected_tea += int(pos)

    if pos == "R":
        break

if collected_tea < 10:
    print(f"Alice didn't make it to the tea party.")
else:
    print(f"She did it! She went to the party.")

print(*[' '.join(row) for row in territory], sep='\n')
