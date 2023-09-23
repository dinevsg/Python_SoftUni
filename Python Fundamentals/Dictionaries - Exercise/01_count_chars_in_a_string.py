mydict = {}
line = input().split()

for w in line:
    for l in w:
        if l in mydict:
            mydict[l] += 1
        else:
            mydict[l] = 1
            
for w, l in mydict.items():
    print(f'{w} -> {l}')
