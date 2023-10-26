from collections import deque

bees = deque(int(x) for x in input().split())
nectar = deque(int(x) for x in input().split())
symbols = deque(x for x in input().split())

result = 0

operations = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x / y,
}

while bees and nectar:
    bee = bees.popleft()
    nec = nectar.pop()

    if nec < bee:
        bees.appendleft(bee)
    elif nec > bee:
        result += abs(operations[symbols.popleft()](bee, nec))

print(f"Total honey made: {result}")

if bees:
    print(f"Bees left: {', '.join(str(x) for x in bees)}")
if nectar:
    print(f"Nectar left: {', '.join(str(x) for x in nectar)}")




