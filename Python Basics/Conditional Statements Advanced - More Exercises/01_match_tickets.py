budget = float(input())
category = input()
people = int(input())

transport = 0
tickets_price = 0

if 1 <= people <= 4:
    transport = budget * 75 / 100

elif 5 <= people <= 9:
    transport = budget * 60 / 100

elif 10 <= people <= 24:
    transport = budget * 50 / 100

elif 25 <= people <= 49:
    transport = budget * 40 / 100

elif people >= 50:
    transport = budget * 25 / 100

if category == "VIP":
    tickets_price = 499.99 * people
elif category == "Normal":
    tickets_price = 249.99 * people

if budget >= tickets_price + transport:
    print(f"Yes! You have {budget - (tickets_price + transport):.2f} leva left.")
elif budget < tickets_price + transport:
    print(f"Not enough money! You need {abs(budget - (tickets_price + transport)):.2f} leva.")



