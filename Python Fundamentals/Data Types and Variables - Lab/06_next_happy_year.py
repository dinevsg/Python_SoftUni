year = int(input())
year += 1
year_ass = str(year)
while len(year_ass) != len(set(year_ass)):
    year += 1
    year_ass = str(year)
print(year)


