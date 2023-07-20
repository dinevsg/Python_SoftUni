nylon = int(input())
paint = int(input())
liquid = int(input())
hours = int(input())

price_nylon = (nylon + 2) * 1.50
price_paint = (paint + paint * 0.1) * 14.50
price_liquid = liquid * 5
bags = 0.40

total_materials = price_liquid + price_paint + price_nylon + bags
price_hours = hours * (total_materials * 0.3)

total_price = price_hours + price_liquid + price_paint + price_nylon + bags

print(total_price)
