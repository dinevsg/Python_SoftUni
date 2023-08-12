n = int(input())
p = int(input())

course = int(n / p)
if n % p != 0:
    course += 1
    print(course)
else:
    print(course)
