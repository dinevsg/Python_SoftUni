def sum_numbers(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def add_and_subtract(n1, n2, n3):
    first_two = sum_numbers(n1, n2)
    return subtract(first_two, third)


first = int(input())
second = int(input())
third = int(input())
print(add_and_subtract(first, second, third))
