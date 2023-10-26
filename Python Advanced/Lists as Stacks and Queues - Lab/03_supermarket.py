from collections import deque

queue = deque()

while True:
    names = input()
    if names == "Paid":
        while queue:
            print(queue.popleft())
        continue
    elif names == "End":
        break
    queue.append(names)
print(f"{len(queue)} people remaining.")
