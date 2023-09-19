stocks = input().split()
check = input().split()

my_dict = {}
for i in range(0, len(stocks), 2):
    stock = stocks[i]
    quantity = stocks[i + 1]
    my_dict[stock] = int(quantity)

for product in check:
    if product in my_dict:
        print(f"We have {my_dict[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")


