n = int(input())
even_list = []
odd_list = []
positive_list = []
negative_list = []

for _ in range(n):
    number = int(input())
    if number >= 0:
        positive_list.append(number)
    else:
        negative_list.append(number)
    if number % 2 == 0:
        even_list.append(number)
    else:
        odd_list.append(number)

command = input()
if command == "even":
    print(even_list)
elif command == "odd":
    print(odd_list)
elif command == "positive":
    print(positive_list)
else:
    print(negative_list)


