juniors = int(input())
seniors = int(input())
race = input()

overall = 0
prise = 0
if race == "trail":
    prise = juniors * 5.50 + seniors * 7
    overall = prise - prise * 5 / 100

elif race == "cross-country":
    if juniors + seniors >= 50:
        prise = (juniors * 8 + seniors * 9.50) - (juniors * 8 + seniors * 9.50) * 25 / 100
        overall = prise - prise * 5 / 100
    elif juniors + seniors < 50:
        prise = juniors * 8 + seniors * 9.50
        overall = prise - prise * 5 / 100

elif race == "downhill":
    prise = juniors * 12.25 + seniors * 13.75
    overall = prise - prise * 5 / 100

elif race == "road":
    prise = juniors * 20 + seniors * 21.50
    overall = prise - prise * 5 / 100

print(f"{overall:.2f}")



