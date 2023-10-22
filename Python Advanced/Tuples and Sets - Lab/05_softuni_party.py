n = int(input())
res = set()

for _ in range(n):
    rc = input()
    res.add(rc)

guest = input()
while guest != "END":
    if guest in res:
        res.remove(guest)
        guest = input()

print(len(res))
for num in sorted(res):
    print(num)
