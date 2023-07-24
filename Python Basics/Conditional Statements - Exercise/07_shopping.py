budget = float(input())
vc_pcs = int(input())
pr_pcs = int(input())
ram_pcs = int(input())

vc_price = vc_pcs * 250
pr_price = pr_pcs * (vc_price * 0.35)
ram_price = ram_pcs * (vc_price * 0.1)

total_price = vc_price + pr_price + ram_price

if vc_pcs > pr_pcs:
    total_price = total_price - (total_price * 0.15)

diff = abs(total_price - budget)

if total_price <= budget:
    print(f"You have {diff:.2f} leva left!")
else:
    print(f"Not enough money! You need {diff:.2f} leva more!")
