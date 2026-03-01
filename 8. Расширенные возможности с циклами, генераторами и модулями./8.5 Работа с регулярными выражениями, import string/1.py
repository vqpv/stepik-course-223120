import re


s = input()

pattern = r"\b\d{13}\b"

print(*re.findall(pattern, s))
