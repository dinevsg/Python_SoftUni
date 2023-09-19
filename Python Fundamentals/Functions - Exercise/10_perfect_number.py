number = int(input())
sum_num = 0

for i in range(1, number):
    if number % i == 0:
        sum_num = sum_num + i
if sum_num == number:
    print(f"We have a perfect number!")
else:
    print(f"It's not so perfect.")
    
