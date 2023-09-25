price_by_product = {}
quantity_by_product = {}

while True:
    line = input()
    if line == "buy":
        break
    products = line.split()
    product = products[0]
    price = float(products[1])
    quantity = int(products[2])

    if product in price_by_product:
        price_by_product[product] = price
        quantity_by_product[product] += quantity
    else:
        price_by_product[product] = price
        quantity_by_product[product] = quantity
for product in price_by_product:
    price = price_by_product[product]
    quantity = quantity_by_product[product]
    total_price = quantity * price
    print(f'{product} -> {total_price:.2f}')
    
