year_tax = int(input())

shoes = year_tax - year_tax * 0.4
clothes = shoes - shoes * 0.2
ball = clothes / 4
acc = ball / 5

total = year_tax + shoes + clothes + ball + acc

print(total)
