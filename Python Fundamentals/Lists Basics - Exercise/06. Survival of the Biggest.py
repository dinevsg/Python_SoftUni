numbers = [int(x) for x in input().split()]
n = int(input())


for _ in range(n):
    min_number = min(numbers)
    numbers.remove(min_number)

for idx in range(len(numbers)):
    num = numbers[idx]
    if idx == len(numbers) - 1:
        print(num)
    else:
        print(num, end=", ")
