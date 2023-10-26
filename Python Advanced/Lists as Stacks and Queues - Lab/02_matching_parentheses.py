# 1 + (2 - (2 + 3) * 4 / (3 + 1)) * 5
string = input()
stack = []

for i in range(len(string)):
    if string[i] == "(":
        stack.append(i)
    elif string[i] == ")":
        start = stack.pop()
        end = i + 1
        print(string[start:end])
