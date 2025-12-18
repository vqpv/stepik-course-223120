s = input()

for i in s:
    if i.lower() in ["a", "e", "i", "o", "u", "y"]:
        print(i, end="")
