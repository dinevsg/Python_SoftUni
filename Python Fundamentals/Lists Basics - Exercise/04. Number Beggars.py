numbers = input().split(", ")
beggars_count = int(input())

numbers_digits = []
for el in numbers:
    numbers_digits.append(int(el))

final_sum = []
starting_index = 0

while starting_index < beggars_count:
    sum_beggars = 0
    for current_index in range(starting_index, len(numbers_digits), beggars_count):
        sum_beggars += numbers_digits[current_index]
    final_sum.append(sum_beggars)
    starting_index += 1
print(final_sum)




