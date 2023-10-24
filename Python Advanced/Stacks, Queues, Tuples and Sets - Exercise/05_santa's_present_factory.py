from collections import deque

materials = deque(int(x) for x in input().split())   # 10 -5 20 15 -30 10
magic_level = deque(int(x) for x in input().split())  # 40 60 10 4 10 0

crafted = []

mix = {
    150: "Doll",
    250: "Wooden train",
    300: "Teddy bear",
    400: "Bicycle",
}

while materials and magic_level:
    material = materials.pop() if magic_level[0] or not materials[0] else 0
    magic = magic_level.popleft() if material or not magic_level[0] else 0
    if not magic:
        continue

    total_ml = magic * material

    if mix.get(total_ml):
        crafted.append(mix[total_ml])
    elif total_ml < 0:
        materials.append(material + magic)
    elif total_ml > 0:
        materials.append(material + 15)

if {"Doll", "Wooden train"}.issubset(crafted) or {"Teddy bear", "Bicycle"}.issubset(crafted):
    print(f"The presents are crafted! Merry Christmas!")
else:
    print(f"No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join([str(x) for x in materials][::-1])}")

if magic_level:
    print(f"Magic left: {', '.join([str(x) for x in magic_level])}")

[print(f"{toy}: {crafted.count(toy)}") for toy in sorted(set(crafted))]




