country = input().split(', ')
city = input().split(', ')

mydict = {country[idx]: city[idx] for idx in range(len(country))}
for co, ci in mydict.items():
    print(f'{co} -> {ci}')
