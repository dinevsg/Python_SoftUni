square_meters_for_greening = float(input())

price_for_greening_whole_yard = square_meters_for_greening * 7.61
discount = price_for_greening_whole_yard * 0.18
total_price_for_greening = price_for_greening_whole_yard - discount

print(f"The final price is {total_price_for_greening} lv.")
print(f"The discount is {discount} lv.")
