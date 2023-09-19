def palindrome(numbers):
    for i in numbers:
        if i[::-1] == i:
            print("True")
        else:
            print(f"False")


numbers = (str(x) for x in input().split(", "))
palindrome(numbers)
