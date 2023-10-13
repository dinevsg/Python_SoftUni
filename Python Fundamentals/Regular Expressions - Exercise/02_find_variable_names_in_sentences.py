import re

line = input()
pattern = r"\b_([A-Za-z\d]+)\b"
result = re.findall(pattern, line)

print(",".join(result))
