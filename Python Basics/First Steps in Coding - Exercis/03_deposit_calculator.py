deposit_amount = float(input())
term_of_deposit = int(input())
annual_interest_estimate = float(input())

total_amount = deposit_amount + term_of_deposit * ((deposit_amount * (annual_interest_estimate / 100)) / 12)

print(total_amount)
