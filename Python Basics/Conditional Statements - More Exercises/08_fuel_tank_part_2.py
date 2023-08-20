fuel_type = input()
liters = float(input())
discount_card = input()

price_gasoline = liters * 2.22
price_diesel = liters * 2.33
price_gas = liters * 0.93


if fuel_type == "Gasoline":
    if discount_card == "Yes":
        price_gasoline -= liters * 0.18
    if 20 <= liters <= 25:
        price_gasoline -= price_gasoline * 8 / 100
    elif liters > 25:
        price_gasoline -= price_gasoline * 10 / 100

    print(f"{price_gasoline:.2f} lv.")

elif fuel_type == "Diesel":
    if discount_card == "Yes":
        price_diesel -= liters * 0.12
    if 20 <= liters <= 25:
        price_diesel -= price_diesel * 8 / 100
    elif liters > 25:
        price_diesel -= price_diesel * 10 / 100

    print(f"{price_diesel:.2f} lv.")

elif fuel_type == "Gas":
    if discount_card == "Yes":
        price_gas -= liters * 0.08
    if 20 <= liters <= 25:
        price_gas -= price_gas * 8 / 100
    elif liters > 25:
        price_gas -= price_gas * 10 / 100

    print(f"{price_gas:.2f} lv.")
