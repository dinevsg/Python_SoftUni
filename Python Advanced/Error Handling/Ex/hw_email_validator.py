import re


class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


class MoreThanOneSymbolError(Exception):
    pass


class InvalidNameError(Exception):
    pass


MIN_LENGTH = 4
VALID_DOMAINS = [".com", ".bg", ".net", ".org"]

pattern = r"[\w+\.]"
pattern_domain = r"\.[a-z]+"

email = input()

while email != "End":

    if email.count("@") > 1:
        raise MoreThanOneSymbolError("Email should contain more than one @ symbol!")
    if len(email.split("@")[0]) < MIN_LENGTH:
        raise NameTooShortError("Name must be more than 4 characters")
    if "@" not in email:
        raise MustContainAtSymbolError("Email must contain @")
    if re.findall(pattern, email[0]) != email.split("@")[0]:
        raise InvalidNameError("Name must contain only letters, digits and underscores!")
    if re.findall(pattern_domain, email)[-1] not in VALID_DOMAINS:
        raise InvalidNameError("Domain must be one of the following: .com, .bg, .org, .net")

    print("Email is invalid")

    email = input()


