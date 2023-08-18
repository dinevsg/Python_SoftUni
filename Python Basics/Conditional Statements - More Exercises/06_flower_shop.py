import math

magnolia_price = int(input()) * 3.25
hyacinth_price = int(input()) * 4
rose_price = int(input()) * 3.50
catus_price = int(input()) * 8

present_price = float(input())

sum_overall = (magnolia_price + hyacinth_price + rose_price + catus_price)
final_revenue = sum_overall - (sum_overall * 5 / 100)

if final_revenue >= present_price:
    print(f"She is left with {math.floor(final_revenue - present_price)} leva.")

elif final_revenue < present_price:
    print(f"She will have to borrow {math.ceil(present_price - final_revenue)} leva.")


