def check_len(mypass):
    return 6 <= len(mypass) <= 10


def check_isalnum(mypass):
    return mypass.isalnum()


def check_two_digits(mypass):
    digits_counter = 0
    for i in mypass:
        if i.isdigit():
            digits_counter += 1
    return digits_counter >= 2


password = input()
is_valid = True

if not check_len(password):
    is_valid = False
    print(f"Password must be between 6 and 10 characters")
if not check_isalnum(password):
    is_valid = False
    print(f"Password must consist only of letters and digits")
if not check_two_digits(password):
    is_valid = False
    print(f"Password must have at least 2 digits")
if is_valid:
    print(f"Password is valid")
