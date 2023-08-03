start = int(input())
end = int(input())
result = int(input())

combs = 0
comb = False

for x in range(start, end + 1):
    for y in range(start, end + 1):
        combs += 1

        if x + y == result:
            print(f"Combination N:{combs} ({x} + {y} = {result})")
            comb = True
            break

    if comb:
        break

if not comb:
    print(f"{combs} combinations - neither equals {result}")
