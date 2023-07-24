n = int(input())
time = input()

if time == "day":
    if n < 20:
        taxi = 0.79 * n + 0.70
        print(f"{taxi:.2f}")
    elif 20 <= n < 100:
        bus = 0.09 * n
        print(f"{bus:.2f}")
    elif n >= 100:
        train = 0.06 * n
        print(f"{train:.2f}")

elif time == "night":
    if n < 20:
        taxi = 0.90 * n + 0.70
        print(f"{taxi:.2f}")
    elif 20 <= n < 100:
        bus = 0.09 * n
        print(f"{bus:.2f}")
    elif n >= 100:
        train = 0.06 * n
        print(f"{train:.2f}")
