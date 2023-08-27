season = input()
group = input()
students = int(input())
stays = int(input())

sport = ""
price = 0

if season == "Winter":
    if group == "boys":
        price = students * 9.60 * stays
        sport = "Judo"

    elif group == "girls":
        price = students * 9.60 * stays
        sport = "Gymnastics"

    elif group == "mixed":
        price = students * 10 * stays
        sport = "Ski"

elif season == "Spring":
    if group == "boys":
        price = students * 7.20 * stays
        sport = "Tennis"

    elif group == "girls":
        price = students * 7.20 * stays
        sport = "Athletics"

    elif group == "mixed":
        price = students * 9.50 * stays
        sport = "Cycling"

elif season == "Summer":
    if group == "boys":
        price = students * 15 * stays
        sport = "Football"

    elif group == "girls":
        price = students * 15 * stays
        sport = "Volleyball"

    elif group == "mixed":
        price = students * 20 * stays
        sport = "Swimming"

if students >= 50:
    price -= price * (50 / 100)

elif 20 <= students < 50:
    price -= price * (15 / 100)

elif 10 <= students < 20:
    price -= price * (5 / 100)

print(f"{sport} {price:.2f} lv.")
