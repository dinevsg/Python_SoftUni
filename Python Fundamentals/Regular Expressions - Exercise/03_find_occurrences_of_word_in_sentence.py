import re

line = input().lower()
target = input().lower()

matches = re.findall(rf"\b{target}\b", line)
print(len(matches))
