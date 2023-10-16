def printed(n, count):
    print(" " * (n - count), end="")
    print(*["*"] * count)


def print_rhombus(x):
    for count in range(1, 1 + n):
        printed(n, count)

    for count in range(n - 1, 0, -1):
        printed(n, count)


n = int(input())
print_rhombus(n)
