def get_min(numbers):
    min_number = float("inf")
    for num in numbers:
        if num < min_number:
            min_number = num
    return min_number

first = int(input())
second = int(input())
third = int(input())

print(get_min([first, second, third]))
