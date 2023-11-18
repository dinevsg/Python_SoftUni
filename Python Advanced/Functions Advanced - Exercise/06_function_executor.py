# def func_executor(*funcs):
#     my_list = []
#     for func, args in funcs:
#         my_list.append(f"{func.__name__} - {func(*args)}")
#     return "\n".join(my_list)
#

def func_executor(*funcs):
    return "\n".join([f"{func.__name__} - {func(*args)}" for func, args in funcs])


def sum_numbers(num1, num2):
    return num1 + num2


def multiply_numbers(num1, num2):
    return num1 * num2


print(func_executor(
    (sum_numbers, (1, 2)),
    (multiply_numbers, (2, 4))
))