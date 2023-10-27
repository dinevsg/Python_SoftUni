def multiply(*args):
    res = 1
    for n in args:
        res *= n
    return res


print(multiply(1, 4, 5))
