pencil_packs = int(input())
marker_packs = int(input())
cleaning_liquid = int(input())
percentage_discount = int(input())

price_pencil_pack = pencil_packs * 5.80
price_marker_pack = marker_packs * 7.20
price_cleaning_liquid = cleaning_liquid * 1.20

price = price_pencil_pack + price_marker_pack + price_cleaning_liquid

total_price = (price - price * (percentage_discount / 100))

print(total_price)
