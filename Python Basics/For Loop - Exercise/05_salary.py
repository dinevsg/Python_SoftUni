tabs = int(input())
init_salary = int(input())

salary = init_salary

for i in range(1, tabs + 1):
    website = input()
    if website == "Facebook":
        salary = salary - 150
    elif website == "Instagram":
        salary = salary - 100
    elif website == "Reddit":
        salary = salary - 50

    if salary <= 0:
        break

if salary <= 0:
    print(f"You have lost your salary.")
else:
    print(salary)
