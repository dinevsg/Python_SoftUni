n = int(input())
parking = set()
for _ in range(n):
    io, lp = input().split(", ")
    if io == "IN":
        parking.add(lp)
    if io == "OUT":
        parking.remove(lp)

if parking:
    print(*parking, sep="\n")
else:
    print(f"Parking Lot is Empty")
