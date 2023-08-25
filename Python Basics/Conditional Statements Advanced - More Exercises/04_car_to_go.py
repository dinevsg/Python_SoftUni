budget = float(input())
season = input()

price = 0
car_type = ""
car_class = ""

if budget <= 100:
    car_class = "Economy class"
    if season == "Summer":
        car_type = "Cabrio"
        price = budget * 35 / 100
    elif season == "Winter":
        car_type = "Jeep"
        price = budget * 65 / 100

elif 100 < budget <= 500:
    car_class = "Compact class"
    if season == "Summer":
        car_type = "Cabrio"
        price = budget * 45 / 100
    elif season == "Winter":
        car_type = "Jeep"
        price = budget * 80 / 100

else:
    car_class = "Luxury class"
    car_type = "Jeep"
    price = budget * 90 / 100

print(car_class)
print(f"{car_type} - {price:.2f}")
