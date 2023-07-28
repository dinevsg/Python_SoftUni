ticket_type = input()
columns = int(input())
rows = int(input())

all_seats = rows * columns
price = 0

if ticket_type == "Premiere":
    price = 12

if ticket_type == "Normal":
    price = 7.50
elif ticket_type == "Discount":
    price = 5

total_sum = price * all_seats

print(f"{total_sum:.2f} leva")
