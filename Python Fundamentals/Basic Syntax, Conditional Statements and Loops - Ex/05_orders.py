order = int(input())

total_price = 0
for _ in range(order):
    price_per_caps = float(input())
    days = int(input())
    caps_per_day = int(input())
    if price_per_caps < 0.01 or price_per_caps > 100.00:
        continue
    if days < 1 or days > 31:
        continue
    if caps_per_day < 1 or caps_per_day > 2000:
        continue
    order_price = days * caps_per_day * price_per_caps
    total_price += order_price
    print(f"The price for the coffee is: ${order_price:.2f}")
print(f"Total: ${total_price:.2f}")
