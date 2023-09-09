def calc(command, n1, n2):
    result = 0
    if command == "multiply":
        result = n1 * n2
    elif command == "divide":
        result = n1 // n2
    elif command == "add":
        result = n1 + n2
    elif command == "subtract":
        result = n1 - n2
    return result


operator = input()
first_num = int(input())
second_num = int(input())

res = calc(operator, first_num, second_num)
print(res)

