string = input()

stack = list(string)

while stack:
    removed_element = stack.pop()
    print(removed_element, end="")
