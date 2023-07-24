import math

vineyard = int(input())
grapes_sq = float(input())
litters_needed = int(input())
employees = int(input())

total_grapes = vineyard * grapes_sq
wine = 40 / 100 * total_grapes / 2.5

if wine < litters_needed:
    print(f"It will be a tough winter! More {math.floor(litters_needed - wine)} liters wine needed.")

elif wine >= litters_needed:
    print(f"Good harvest this year! Total wine: {wine:.0f} liters.")
    print(f"{wine - litters_needed:.0f} liters left -> {math.ceil((wine - litters_needed) / employees)} liters per person.")
