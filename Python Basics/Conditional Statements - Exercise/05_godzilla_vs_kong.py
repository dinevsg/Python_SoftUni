budget = float(input())
statists = int(input())
clothes_one = float(input())

decor_price = budget * 0.1
clothing_price = clothes_one * statits

if statists > 150:
    clothing_price = clothing_price * 0.9

overall_price = decor_price + clothing_price
diff = abs(budget - overall_price)

if budget >= overall_price:
    print('Action!')
    print(f'Wingard starts filming with {diff:.2f} leva left.')
else:
    print('Not enough money!')
    print(f'Wingard needs {diff:.2f} leva more.')
