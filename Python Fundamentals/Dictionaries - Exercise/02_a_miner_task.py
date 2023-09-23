mydict = {}

while True:
    line = input()
    if line == 'stop':
        break
    quantity = int(input())

    if line in mydict:
        mydict[line] += quantity
    else:
        mydict[line] = quantity

for line, quantity in mydict.items():
    print(f'{line} -> {quantity}')
    
