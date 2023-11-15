from collections import deque

clothes = deque([int(x) for x in input().split()])
rack_capacity = int(input())
current_rack = 1
current_rack_capacity = rack_capacity
while clothes:
    for cloth in clothes.copy():

        if rack_capacity >= cloth:
            clothes.popleft()
            rack_capacity -= cloth
        else:
            rack_capacity = current_rack_capacity - clothes.popleft()
            current_rack += 1

print(current_rack)
