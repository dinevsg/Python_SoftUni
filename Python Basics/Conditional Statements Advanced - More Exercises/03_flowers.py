chrys = int(input())
roses = int(input())
tulips = int(input())
season = input()
holiday = input()

chrys_price = 0
roses_price = 0
tulips_price = 0


if season == "Summer" or season == "Spring":
    chrys_price = chrys * 2.00
    roses_price = roses * 4.10
    tulips_price = tulips * 2.50

elif season == "Autumn" or season == "Winter":
    chrys_price = chrys * 3.75
    roses_price = roses * 4.50
    tulips_price = tulips * 4.15

overall_price = 0

if holiday == "Y":
    chrys_price += chrys_price * 15 / 100
    roses_price += roses_price * 15 / 100
    tulips_price += tulips_price * 15 / 100
    overall_price = tulips_price + chrys_price + roses_price

    if season == "Spring" and tulips >= 7:
        overall_price -= overall_price * 5 / 100

    if season == "Winter" and roses >= 10:
        overall_price -= overall_price * 10 / 100

    if tulips + chrys + roses > 20:
        overall_price -= overall_price * 20 / 100

else:
    overall_price = tulips_price + chrys_price + roses_price

    if season == "Spring" and tulips >= 7:
        overall_price -= overall_price * 5 / 100

    if season == "Winter" and roses >= 10:
        overall_price -= overall_price * 10 / 100

    if tulips + chrys + roses > 20:
        overall_price -= overall_price * 20 / 100

print(f"{overall_price + 2:.2f}")
