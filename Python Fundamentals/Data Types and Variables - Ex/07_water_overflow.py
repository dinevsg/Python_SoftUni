water_tank = 255
n = int(input())
tank = 0

for _ in range(n):
    liters = int(input())
    if tank + liters > water_tank:
        print("Insufficient capacity!")
    else:
        tank += liters

print(tank)
