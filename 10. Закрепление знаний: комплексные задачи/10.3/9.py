import re


q = int(input())

pattern = r"[A-Z]\d{2}"

for _ in range(q):
    s = input()
    print("Yes" if re.fullmatch(pattern, s) else "No")
