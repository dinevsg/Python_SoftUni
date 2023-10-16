n, m = [int(num) for num in input().split()]

first = set()
second = set()

for _ in range(n):
    nums = int(input())
    first.add(nums)

for _ in range(m):
    nums = int(input())
    second.add(nums)


print(*first.intersection(second), sep="\n")

