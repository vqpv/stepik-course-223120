import re


s = input()

pattern = r"[0-3][0-9]\.[0-1][0-9]\.\d{4}"

print("Найденные даты:", *re.findall(pattern, s))
