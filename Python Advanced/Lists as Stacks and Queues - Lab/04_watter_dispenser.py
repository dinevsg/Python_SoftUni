from collections import deque

water_quantity = int(input())
name = input()
people = deque()

while name != "Start":
    people.append(name)
    name = input()

command = input()

while command != "End":
    data = command.split()
    if len(data) == 1:
        liters = int(data[0])

        if water_quantity >= liters:
            water_quantity -= liters
            person = people.popleft()
            print(f"{person} got water")
        else:
            person = people.popleft()
            print(f"{person} must wait")

    else:
        liters_refill = int(data[1])
        water_quantity += liters_refill

    command = input()
print(f"{water_quantity} liters left")
