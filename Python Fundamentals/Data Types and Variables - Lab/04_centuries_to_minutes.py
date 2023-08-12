cent = int(input())
years = cent * 100
days = int(years * 365.2422)
hours = days * 24
minutes = hours * 60

print(f"{cent} centuries = {years} years = {days:.0f} days = {hours} hours = {minutes} minutes")
