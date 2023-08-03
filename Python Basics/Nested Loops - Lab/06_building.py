floors = int(input())
rooms_per_floor = int(input())

flat = ''

for floor in range(floors, 0, -1):
    for rooms in range(0, rooms_per_floor):
        flat_name = f"{floor}{rooms}"
        if floor == floors:
            print(f"L{floor}{rooms}", end=' ')
        elif floor % 2 != 0:
            print(f"A{floor}{rooms}", end=' ')
        elif floor % 2 == 0:
            print(f"O{floor}{rooms}", end=' ')
    print()
