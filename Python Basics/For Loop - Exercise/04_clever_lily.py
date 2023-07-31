age = int(input())
wash_machine = float(input())
toy_price = int(input())

toys = 0
money = 0
total_sum = 0
brother = 0

for i in range(1, age + 1):
    if i % 2 != 0:
        toys += 1
    else:
        brother += 1
        money = money + 10
        total_sum = total_sum + money

result = (toys * toy_price) + total_sum - brother

diff = abs(result - wash_machine)
if result >= wash_machine:
    print(f"Yes! {diff:.2f}")
else:
    print(f"No! {diff:.2f}")
