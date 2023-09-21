text = input()

products = {}

while text != "statistics":
    args = text.split(": ")
    product = args[0]
    quantity = int(args[1])
    if product not in products:
        products[product] = quantity
    else:
        products[product] += quantity

    text = input()

print(f"Products in stock:")

for product, quantity in products.items():
    print(f"- {product}: {quantity}")

print(f"Total Products: {len(products.keys())}")
print(f"Total Quantity: {sum(products.values())}")
