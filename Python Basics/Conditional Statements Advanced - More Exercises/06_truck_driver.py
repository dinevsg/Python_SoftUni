season = input()
km = float(input())

salary = 0
if season == "Spring" or season == "Autumn":
    if km <= 5000:
        salary = 0.75 * km

    elif 5000 < km <= 10000:
        salary = 0.95 * km

    else:
        salary = 1.45 * km

elif season == "Summer":
    if km <= 5000:
        salary = 0.90 * km

    elif 5000 < km <= 10000:
        salary = 1.10 * km

    else:
        salary = 1.45 * km

elif season == "Winter":
    if km <= 5000:
        salary = 1.05 * km

    elif 5000 < km <= 10000:
        salary = 1.25 * km

    else:
        salary = 1.45 * km

print(f"{(salary - (salary * 10 / 100)) * 4:.2f}")
