numbers = int(input())
result = []

while numbers > 0:
    n = len(result) + 1
    shell_value = min(2 * (n ** 2), numbers)
    result.append(shell_value)
    numbers -=shell_value
print(result)
