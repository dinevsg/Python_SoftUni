def is_even(number):
    return number % 2 == 0


n = [int(x) for x in input().split()]
print(list(filter(is_even, n)))
