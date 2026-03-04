import re


s = input()

pattern = r"^\w+@\w+\.\w+"

print("Email корректен." if re.fullmatch(pattern, s) else "Email некорректен.")
