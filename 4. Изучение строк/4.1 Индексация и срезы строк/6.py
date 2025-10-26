s = input()

l = len(s)

if l > 4:
    print(s[:2] + "*" * (l - 4) + s[-2:])
else:
    print(s)
