from collections import deque

chocolates = deque(int(x) for x in input().split(", "))
milks = deque(int(x) for x in input().split(", "))

milkshakes = 0

while milkshakes != 5 and chocolates and milks:
    milk = milks.popleft()
    chocolate = chocolates.pop()

    if chocolate <= 0 and milk <= 0:
        continue
    elif chocolate <= 0:
        milks.appendleft(milk)
        continue
    elif milk <= 0:
        chocolates.append(chocolate)
        continue

    if chocolate == milk:
        milkshakes += 1
    else:
        milks.append(milk)
        chocolates.append(chocolate - 5)

if milkshakes == 5:
    print(f"Great! You made all the chocolate milkshakes needed!")
else:
    print(f"Not enough milkshakes.")

print(f"Chocolate: {', '.join(str(ch) for ch in chocolates) or 'empty'}")
print(f"Milk: {', '.join(str(m) for m in milks) or 'empty'}")
