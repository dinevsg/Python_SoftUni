n = float(input())
while True:
    if n < 0:
        print("Negative number!")
        break
    print(f"Result: {n * 2:.2f}")
    n = float(input())
