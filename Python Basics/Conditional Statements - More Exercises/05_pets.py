import math

days = int(input())
food_left = int(input())
dog_food = float(input()) * days
cat_food = float(input()) * days
turtle_food = float(input()) / 1000 * days

total = dog_food + cat_food + turtle_food

if food_left >= total:
    print(f"{math.floor(food_left - total)} kilos of food left.")

elif food_left < total:
    print(f"{math.ceil(total - food_left)} more kilos of food are needed.")



