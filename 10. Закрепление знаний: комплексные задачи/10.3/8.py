s = input()

print(*[i for i in s.split(",") if "dist=" in i])
