book = input()

count = 0
input_line = input()
isFound = False

while input_line != "No More Books":
    if book == input_line:
        isFound = True
        break

    count = count + 1
    input_line = input()

if isFound:
    print(f"You checked {count} books and found it.")
else:
    print("The book you search is not here!")
    print(f"You checked {count} books.")
