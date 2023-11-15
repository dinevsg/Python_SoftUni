from collections import deque

pumps = deque([[int(x) for x in input().split()] for _ in range(int(input()))])
pumps_copy = pumps.copy()
tank = 0
start_i = 0
while pumps_copy:
    petrol, distance = pumps_copy.popleft()
    tank += petrol
    if tank >= distance:
        tank -= distance
    else:
        pumps.rotate(-1)
        pumps_copy = pumps.copy()
        start_i += 1
        tank = 0
print(start_i)


