word = input()

letters = 0

for i in range(0, len(word)):
    if word[i] == "a":
        letters += 1
    if word[i] == "e":
        letters += 2
    if word[i] == "i":
        letters += +3
    if word[i] == "o":
        letters += 4
    if word[i] == "u":
        letters += 5

print(letters)
