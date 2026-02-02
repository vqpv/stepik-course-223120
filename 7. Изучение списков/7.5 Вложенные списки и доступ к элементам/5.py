ingredients = [
    ["курица", "говядина", "свинина"],
    ["лук", "чеснок", "морковь"],
    ["соль", "перец", "паприка"]
]

result = False

s = input()

for i in ingredients:
    if s in i:
        result = True
        break

print(result)
