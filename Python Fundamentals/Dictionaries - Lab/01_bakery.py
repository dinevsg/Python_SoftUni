data = input().split()
data_new = {}
for index in range(0, len(data), 2):
    key = data[index]
    value = data[index + 1]
    data_new[key] = int(value)

print(data_new)