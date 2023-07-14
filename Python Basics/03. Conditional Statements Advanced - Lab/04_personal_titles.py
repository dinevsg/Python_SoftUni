age = float(input())
sex = input()

if sex == "m":
    if 16 <= age:
        print("Mr.")
    elif 16 > age:
        print("Master")

if sex == "f":
    if 16 <= age:
        print("Ms.")
    elif 16 > age:
        print("Miss")
