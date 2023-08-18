fuel = input()
liters = int(input())

if fuel != "Diesel" and fuel != "Gasoline" and fuel != "Gas":
    print("Invalid fuel!")
    raise SystemExit
if liters >= 25:
    print(f"You have enough {fuel.lower()}.")
elif liters < 25:
    print(f"Fill your tank with {fuel.lower()}!")

