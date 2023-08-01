constant_number = int(input())
current_sum = 0

while True:
    current_number = int(input())
    current_sum = current_sum + current_number

    if current_sum >= constant_number:
        print(current_sum)
        break
