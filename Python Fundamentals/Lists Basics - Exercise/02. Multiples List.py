first = int(input())
second = int(input())

new_list = []

for num in range(1, second + 1):
    new_list.append(num * first)
print(new_list)
