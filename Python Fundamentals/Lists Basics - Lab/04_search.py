n = int(input())
word = input()

some_list = []
string_contain = []

for _ in range(n):
    all_strings = input()
    some_list.append(all_strings)
    if word in all_strings:
        string_contain.append(all_strings)
print(some_list)
print(string_contain)

