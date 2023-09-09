def calc_amount(product, quantity):
    result = 0
    if product == "water":
        result = quantity * 1
    elif product == "coffee":
        result = quantity * 1.50
    elif product == "coke":
        result = quantity * 1.40
    elif product == "snacks":
        result = quantity * 2
    return result


product_buy = input()
quantity_buy = int(input())

total = calc_amount(product_buy, quantity_buy)
print(f"{total:.2f}")

