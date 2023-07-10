number_of_packages_dogfood = int(input())
number_of_packages_catfood = int(input())

price_dogfood = number_of_packages_dogfood * 2.50
price_catfood = number_of_packages_catfood * 4
total_price = price_catfood + price_dogfood

print(f"{total_price} lv.")