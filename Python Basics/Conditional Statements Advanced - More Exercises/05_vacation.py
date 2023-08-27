budget = float(input())
season = input()

price = 0
location = ""
place = ""

if budget <= 1000:
    place = "Camp"
    if season == "Summer":
        location = "Alaska"
        price = budget * (65 / 100)

    elif season == "Winter":
        location = "Morocco"
        price = budget * (45 / 100)

elif 1000 < budget <= 3000:
    place = "Hut"
    if season == "Summer":
        location = "Alaska"
        price = budget * (80 / 100)

    elif season == "Winter":
        location = "Morocco"
        price = budget * (60 / 100)

else:
    place = "Hotel"
    price = budget * (90 / 100)
    if season == "Summer":
        location = "Alaska"

    elif season == "Winter":
        location = "Morocco"


print(f"{location} - {place} - {price:.2f}")
