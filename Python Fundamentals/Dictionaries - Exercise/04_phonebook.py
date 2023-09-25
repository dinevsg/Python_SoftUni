phonebook = {}

while True:
    line = input()
    info = line.split("-")
    if len(info) == 1:
        n = int(line)
        break

    name = info[0]
    number = info[1]
    phonebook[name] = number

for i in range(n):
    name = input()
    if name in phonebook:
        print(f"{name} -> {phonebook[name]}")
    else:
        print(f"Contact {name} does not exists.")
        
