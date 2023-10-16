from collections import deque

first = set(int(x) for x in input().split())
second = set(int(x) for x in input().split())

commands = {
    "Add First": lambda x: [first.add(int(el)) for el in data],
    "Add Second": lambda x: [second.add(int(el)) for el in data],
    "Remove First": lambda x: [first.discard(int(el)) for el in data],
    "Remove Second": lambda x: [second.discard(int(el)) for el in data],
    "Check Subset": lambda x: print(first.issubset(second) or second.issubset(first))
}

for _ in range(int(input())):
    first_com, second_com, *data = input().split()
    command = first_com + " " + second_com

    commands[command]([int(el) for el in data])

print(*sorted(set(first)), sep=", ")
print(*sorted(set(second)), sep=", ")
