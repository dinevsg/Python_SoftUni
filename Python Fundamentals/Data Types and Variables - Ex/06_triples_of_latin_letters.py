start = 97
n = int(input())

for i in range(start, start + n):
    for j in range(start, start + n):
        for k in range(start, start + n):
            print(f"{chr(i)}{chr(j)}{chr(k)}")
