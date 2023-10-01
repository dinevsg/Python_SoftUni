company_users = {}

while True:
    line = input()
    if line == 'End':
        break
    info = line.split(' -> ')
    company = info[0]
    employee = info[1]
    if company not in company_users:
        company_users[company] = []
    if employee not in company_users:
        company_users[company].append(employee)
    else:
        continue

for company, employee in company_users.items():
    print(company)
    for employees in employee:
        print(f' -- {employees}')
