from collections import deque

cup_cap = deque(int(cup) for cup in input().split())
bottle_cap = deque(int(bottle) for bottle in input().split())
cups = cup_cap.copy()
bottles = bottle_cap.copy()
wasted = 0
for bottle in bottle_cap:
    while cups and bottles:
        reduced = bottles[-1] - (cups[0])
        bottles.pop()
        if reduced >= 0:
            wasted += reduced
            cups.popleft()
        else:
            reduced += bottles[-1]
            bottles.pop()
            if reduced >= 0:
                wasted += reduced
                cups.popleft()
            elif reduced < 0:
                reduced += bottles[-1]
                bottles.pop()
                cups.popleft()
    if bottles:
        print(f"Bottles: {' '.join([str(bottle) for bottle in bottles])}\nWasted litters of water: {wasted}")
        raise SystemExit
    if cups:
        print(f"Cups: {' '.join([str(cup) for cup in cups])}\nWasted litters of water: {wasted}")
        raise SystemExit




