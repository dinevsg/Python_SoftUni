div = int(input())
bound = int(input())

result = 0
for i in range(1, bound +1):
    if i % div == 0:
        result = i
print(result)
