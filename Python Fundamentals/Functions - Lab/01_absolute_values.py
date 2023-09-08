numbers_as_string = input().split()
number = []

for num_as_str in numbers_as_string:
    number.append(abs(float(num_as_str)))

print(number)
