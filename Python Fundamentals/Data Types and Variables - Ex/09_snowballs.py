n = int(input())
best_ball = float("-inf")
result = ""

for ball in range(n):
    weight = int(input())
    time = int(input())
    quality = int(input())
    value = (weight // time) ** quality
    if value > best_ball:
        best_ball = value
        result = f"{weight} : {time} = {value} ({quality})"
print(result)
