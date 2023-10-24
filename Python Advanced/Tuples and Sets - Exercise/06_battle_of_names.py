even = set()
odd = set()

for row in range(1, int(input()) + 1):
    ascii_name_sum = sum(ord(el) for el in input()) // row

    if ascii_name_sum % 2 == 0:
        even.add(ascii_name_sum)
    else:
        odd.add(ascii_name_sum)

if sum(odd) > sum(even):
    print(*odd.difference(even), sep=", ")
else:
    print(*even.symmetric_difference(odd), sep=", ")
